import requests

i = 1 # to get Bitcoin data
r = requests.get(f"https://api.coinmarketcap.com/data-api/v3/cryptocurrency/detail?id={i}")
js = r.json()
price = js["data"]["statistics"]["price"]

print(js)
