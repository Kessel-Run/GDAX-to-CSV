#!/usr/bin/env python3

import requests
import time
from time import strftime
import csv

# name = input("Enter product (ex. BTC-USD): ")
# name1 = input("Enter path for CSV (ex. /Users/kesselrun/Desktop): ")
product = "BTC-USD"

rawticker = requests.get('https://api.gdax.com/products/' + product + '/ticker').json()
price2 = rawticker['price']
print(price2)

ofile  = open('/Users/kesselrun/Desktop/' + product + strftime("%Y%m%d") + '.csv', "w")
output = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
col1 = ("trade_id","sequence","time","product_id","last_size","best_bid","best_ask")
output.writerow(col1)
ofile.close()

sequence = 0

def main (price2, sequence):
    try:
        rawticker = requests.get('https://api.gdax.com/products/' + product + '/ticker').json()
    except AttributeError:
        pass
        main(price2, sequence)
    price1 = rawticker['price']
    if (price2 != price1):
        for key,value in rawticker.items():
            if key == "trade_id":
                trade_id = value
            # if key == "sequence":
            #     sequence = value
            if key == "time":
                time1 = value
            if key == "product_id":
                product_id = value
            # if key == "side":
            #     side = value
            if key == "size":
                last_size = value
            if key == "bid":
                best_bid = value
            if key == "ask":
                best_ask = value
        sequence1 = sequence+1
        ofile1  = open('/Users/kesselrun/Desktop/' + product + strftime("%Y%m%d") + '.csv', "a")
        output1 = csv.writer(ofile1, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        col = (trade_id,sequence1,time1,product,last_size,best_bid,best_ask)
        output1.writerow(col)
        ofile1.close()
        print (price1)
        return opt1(price1, sequence1)
    else:
        return opt2(price1, sequence)

def opt1(price1, sequence1):
    time.sleep(1)
    main(price1, sequence1)
    
def opt2(price1, sequence):
    time.sleep(1)
    main(price1, sequence)
    
main(price2,sequence)
