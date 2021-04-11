#Function
import yfinance as yf
import pandas as pd

def stock_info_to_csv (tickerStrings, file_name):
    df_list = list()
    for ticker in tickerStrings:
        data = yf.download(ticker, group_by="Ticker", period='5y')
        data['Ticker'] = ticker  #add column with ticker
        df_list.append(data)
        
    #combine all dataframes into a single dataframe
    df = pd.concat(df_list)
    
    #save to csv
    df.to_csv(file_name)

    
    
#Webscraping Yahoo! Finance-Most Active Stocks with Beautiful Soup
from bs4 import BeautifulSoup
import requests

url = 'https://finance.yahoo.com/most-active'
header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'
         }
response = requests.get(url, headers=header)
soup = BeautifulSoup(response.content, 'lxml')

#iterate over dataframe and append tickers to list
symbols = list()
for item in soup.select('.simpTblRow'):
    symbols.append(item.select('[aria-label=Symbol]')[0].get_text())

#Output stock info to csv with yfinance
stock_info_to_csv(symbols, 'ticker_active.csv')



#DOW 30 dataframe from wikipedia
df = pd.read_html('https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average')[1]
#grab tickers into a list
tickers = df.Symbol.to_list()

#Output stock info to csv with yfinance
stock_info_to_csv(tickers, 'ticker_dow.csv')


