#!/usr/bin/env python3
import requests
import pandas as pd
from pandas.io.json import json_normalize

url = "http://webservice.catalogueoflife.org/col/webservice?name=apidae&format=json&response=full"

response = requests.get(url)
json_data = response.json()

df = json_normalize(json_data['results'])
# df = df[df.columns[::-1]]
df.to_csv("bees.csv")


