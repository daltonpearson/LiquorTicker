import lxml
import requests
from lxml import html
import time
from credentials import *
import tweepy

PRODUCT = 545392
POSTAL = 'N0N1R0'
SEARCH = f'http://lcbosearch.com/stores/with/{PRODUCT}/near?q={POSTAL}'

# consumer_key= ''
# consumer_secret= ''
# access_token= ''
# access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def search():
    page = requests.get(SEARCH)
    tree = html.fromstring(page.content)
    store_link = tree.xpath('//td[@class="store-name-col"]/a/@href')[0]
    store_name = store_link[11:].replace('-', ' ')
    distance=float(tree.xpath('//td[@class="store-distance-col"]/text()')[0][19:-38])
    update = f'Berry Blast is in stock at the {store_name} LCBO, {distance}km away: http://lcbosearch.com{store_link}'
    print(update)
    if distance <= 100:
        api.update_status(update)


# search()
# api.update_status('Test Tweet')
while True:
    search()
    time.sleep(3600)