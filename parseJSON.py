import json
import requests
import time


# Declar API Key & Query
key = 'AIzaSyBKOK-XXXXX'
query = 'Schools+in+Cairo'
url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query=' + str(query) + '&key=' + str(key)

# Parse JSON
jsonfile = requests.get(url)
f = jsonfile.json()


# Assign Page Token for to fetch results in the next page if exits
try:
    pagetoken = f['next_page_token']
except KeyError:
    pagetoken = ''
pass


# Recursive Function
def getjson(url, pagetoken, key, query):

    time.sleep(3)  # API has requests per second limitation

    if pagetoken == '':
        print('url', url)
        pass

    else:

        print('e1url', url)

        # Reset URL
        url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query=' + str(query) + '&key=' + str(key)
        url = url + '&pagetoken=' + pagetoken

        jsonfile = requests.get(url)
        f = jsonfile.json()

        # append array with desired data from JSON
        for count, name in enumerate(f['results']):
            names.append((f['results'][count]['name']))
            address.append(f['results'][count]['formatted_address'])

        # print(f) #DEBUG
        # Assign NEW Page Token
        try:
            pagetoken = f['next_page_token']
        except KeyError:
            pagetoken = ''
        pass

        # Recursive call
        getjson(url, pagetoken, key, query)


# Declare lists
names = []
address = []

if len(f['results']) > 0:
    for count, name in enumerate(f['results']):
        names.append((f['results'][count]['name']))
        address.append(f['results'][count]['formatted_address'])
else:
    print('No result founds')


# Function Call
getjson(url, pagetoken, key, query)


# Print Results
for i in range(len(names)):
    print('"' + names[i] + '", "' + address[i] + '"')
