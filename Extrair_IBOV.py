# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 17:38:38 2021

@author: Eduardo Morais
"""
import yfinance as yf

#importo as bibliotecas que irei usar
import pandas as pd

#Lista IBOV x CodYF
pd.set_option('max_columns', None)
ibov = pd.read_excel('C:/Users/eduar/OneDrive/Área de Trabalho/Area Trab/Data Science/CodigosYF.xlsx',sheet_name = "IFNC")
ColYF = ibov["Nome YF"]

for x in ColYF:
    print(x)    
    stock = yf.Ticker(x)    
#get historical market data
    hist = stock.history(period="max")
    hist.to_excel(r'C:/Users/eduar/Downloads/IFNC/'+x+'.xlsx', index = True)
    
#for x in  ColYF:
 #   x= pd.read_excel('C:/Users/Eduardo Morais/Downloads/IBOV/'+x+'.xlsx') 
   #print(x)
   
#Path= r'C:/Users/Eduardo Morais/OneDrive/Área de Trabalho/Data Science/'

