import cbpro
import numpy as np
import smtplib
from email.message import EmailMessage

# import for environment variables and waiting
import os, time

# used to parse XML feeds
import xml.etree.ElementTree as ET
from nltk.util import pr

# get the XML feed and pass it to Element tree
import requests

# date modules that we'll most likely need
from datetime import date, datetime, timedelta

# used to grab the XML url list from a CSV file
import csv

# numpy for sums and means
# import numpy as np

# nlp library to analyse sentiment
# import nltk
# from nltk.sentiment import SentimentIntensityAnalyzer

# used for executing the code
from itertools import count

############################################
#     USER INPUT VARIABLES LIVE BELOW      #
# You may edit those to configure your bot #
############################################


# select what coins to look for as keywords in articles headlines
# The key of each dict MUST be the symbol used for that coin on Binance
# Use each list to define keywords separated by commas: 'XRP': ['ripple', 'xrp']
# keywords are case sensitive
keywords = {
    'LINK': ['ripple', 'xrp', 'XRP', 'Ripple', 'RIPPLE'],
    'BTC': ['BTC', 'bitcoin', 'Bitcoin', 'BITCOIN'],
    'XLM': ['Stellar Lumens', 'XLM'],
    'BCH': ['Bitcoin Cash', 'BCH'],
    'ETH': ['ETH', 'Ethereum'],
    'LTC': ['LTC', 'Litecoin']
}

DEPOSIT_AMOUNT = 100

# The Buy amount in the PAIRING symbol, by default USDT
# 100 will for example buy the equivalent of 100 USDT in Bitcoin.
QUANTITY = 30

# define what to pair each coin to
# AVOID PAIRING WITH ONE OF THE COINS USED IN KEYWORDS
PAIRING = 'USD'
COIN = 'LINK-USD'


# define how often to run the code (check for new + try to place trades)
# in minutes
REPEAT_EVERY = 10

SELL_AT_MARGIN = 0.700000000000000
BUY_AT_MARGIN = 0.900000000000000


############################################
#        END OF USER INPUT VARIABLES       #
#             Edit with care               #
############################################

# current price of CRYPTO pulled through the websocket
CURRENT_PRICE = {}

auth_client = cbpro.AuthenticatedClient("694c385d086a8b91b04aea19627e7b1", "HXDgbSl2WXfo2VZvJ3Urg83onNVtEa75VptSEJPszFu4e5w4a+p/BntmtGgV2im+63vJrhsBCIb9gPhi4hYf9A==", "lsh9tcse5c")


def subscribe():
    ticker = auth_client.get_product_order_book(product_id=COIN, level=3)
    
    # get_product_ticker(product_id=COIN)
    print(ticker)

if __name__ == '__main__':
    print('Press Ctrl-Q to stop the script')
    for i in count():
        subscribe()

# import sys
# import time

# from fixsim as fix

# import quickfix as fix 
# import quickfix42 as fix42


# class Application(fix.Application):

#     def onCreate(self, sessionID): return

#     def onLogon(self, sessionID):
#         self.sessionID = sessionID
#         print ("Successful Logon to session '%s'." % sessionID.toString())
#         return
#     def onLogout(self, sessionID): return

#     def toAdmin(self, sessionID, message): return

#     def fromAdmin(self, sessionID, message): return

#     def toApp(self, sessionID, message):
#         print ("Sent the following message: %s" % message.toString())
#         return
#     def fromApp(self, message, sessionID):
#         print ("Received the following message: %s" % message.toString())
#         return

