#!/usr/bin/python3
import requests


url = "http://158.69.76.135/level0.php"
data_key = {"id":"2089"}

for i in range(2):
    try:
        requests.post(url, data = data_key)
        print("success")
    except:
        print("fail")
