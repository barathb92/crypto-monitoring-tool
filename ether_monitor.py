import json
import requests
import time

max = 0.0;

while True:
	response = requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD')
	data = response.json()
	if (float (data['USD']) > max):
		max = float (data['USD'])
		print ('Max Price is ', max)
	elif(float (max * 0.7 > data['USD'])):
		print ('Price Drop Alert!!!')

	time.sleep(20)