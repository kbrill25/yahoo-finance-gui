#import necessary packages
import yfinance as yf
from yahoo_fin.stock_info import get_data
import yahoo_fin.stock_info as stockinfo
import matplotlib.pyplot as plt
import seaborn
from tkinter import *
from tkinter import ttk
import json
import pandas as pd

#create root 
root = Tk()
root.title("Stock Information Application")
root.geometry("600x200")


#function to search user stock ticker using Yahoo Finance
def stockSearch():
    stockLabel = Label(root,text=stock.get())
    stockLabel.grid(row=10,column=0,columnspan=5)
    
    #convert to uppercase
    stockTicker = stock.get()
    stockTicker = stockTicker.upper()
    
    #utilize Yahoo Finance
    stockData = get_data(stockTicker)
    
    #quote table
    stockQuoteData = stockinfo.get_quote_table(stockTicker)
    
    #extract the data that interests us
    beta = stockQuoteData['Beta (5Y Monthly)']
    eps = stockQuoteData['EPS (TTM)']
    marketcap= stockQuoteData['Market Cap']
    peRatio = stockQuoteData['PE Ratio (TTM)']
    
    oneYearTarget = stockQuoteData['1y Target Est']
    yearRange = stockQuoteData['52 Week Range']
    
    print(stockQuoteData)
    
    myLabel1 = Label(root,text=f"Beta: {beta} \t EPS: {eps} \t Market Capitalization: {marketcap} \tPE Ratio: {peRatio}")
    myLabel2 = Label(root,text=f"One Year Target: {oneYearTarget} \t 52 Week Range {yearRange}")
    myLabel1.grid(row=12,column=0,columnspan=5)
    myLabel2.grid(row=13,column=0,columnspan=5)

    return

stock = Entry(root)
stock.grid(row=0,column=0)

stockButton = Button(root,text="Search Stock Ticker",command=stockSearch)
stockButton.grid(row=0,column=1)

root.mainloop()
