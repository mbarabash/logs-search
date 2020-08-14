import requests
import json
import time
import os


def search(valuesdict):
	response = requests.get('https://logs.tf/api/v1/log?')
	data = response.json()
	ids = []
	for x in data['logs']:
		ids.append(x['id'])
	return ids
		