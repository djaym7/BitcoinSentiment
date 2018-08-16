import tweepy
from textblob import TextBlob
import requests
import json
import time


def funcx():
    # Step 1 - Authenticate
    consumer_key= 'yApSMhd4XyN4iI6Vo5lCW0XKP'
    consumer_secret= '5q9B6vStgsRd0RiraDakXqXHd6EqSPWicFsddMIgQr1ZyxmaWf'
    
    access_token='122633234-YzOnE2sFeQTssJG2O9lQj6aP7nAfHwyDUrUg6bgc'
    access_token_secret='8SYdlcLcBAklpTnlOe5U1Z0vWZgkI76xM2QHU85pFcbrG'
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    
    api = tweepy.API(auth)
    
    polarityList = list()
    bitcoin_tweets = api.search('Bitcoin',per_page=20)
    btc_tweets = api.search('Btc')
    
    
    def addToList(tweets):
        for tweet in tweets:
            #print(tweet.text)
            polarityList.append(TextBlob(tweet.text).sentiment.polarity)
    
    addToList(bitcoin_tweets)
    addToList(btc_tweets)
            
    print("Total tweets read : {}".format(len(polarityList)))
    print("Overall sentiment polarity :{} ".format(sum(polarityList)/len(polarityList)))
    
    
    ############################3
    response  = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    x = json.loads(response.text)
    print('Current Btc price : ')
    print(float(x['bpi']['USD']['rate'].replace(",","")))

while(True):
    funcx()
    #time.sleep(3600)

'''
from twitter import Twitter, OAuth                                                                                                                                                                                                       

oauth = OAuth(access_token, access_token_secret, consumer_key, consumer_secret)
t = Twitter(auth=oauth)

query = t.search.tweets(q='btc')

for s in query['statuses']:
    print(s['created_at'], s['text'], '\n')


'''