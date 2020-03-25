#!/usr/bin/env python
# coding: utf-8

import tweepy
from credentials import twitter

auth = tweepy.OAuthHandler(twitter.consumerKey, twitter.consumerSecret)
auth.set_access_token(twitter.accessKey, twitter.accessSecret)
api = tweepy.API(auth)


def return_trends():
    trends_on_brasil = api.trends_place(WOEID_brasil)
    trends = []
    for trend_item in trends_on_brasil[0]['trends']:
        name = trend_item['name']
        url = trend_item['url']
        promoted_content = trend_item['promoted_content']
        query = trend_item['query']
        tweet_volume = trend_item['tweet_volume']

        trends_data = {
            'name': name,
            'url': url,
            'promoted_content': url,
            'query': query,
            'tweet_volume': tweet_volume
        }
        trends.append(trends_data)
    return trends


def return_relevant_tweets_on_trend(trend_name):
    tweets_list_on = []
    most_relevant_tweets = api.search(
        q=trend_name, lang='pt', result_type='popular')
    for tweet in most_relevant_tweets:
        if tweet.metadata['iso_language_code'] == 'pt':
            created_at = tweet.created_at
            id = tweet.id
            id_str = tweet.id_str
            text = tweet.text

            tweet_data = {
                'created_at': created_at,
                'id': id,
                'id_str': id_str,
                'text': text

            }
            tweets_list_on.append(tweet_data)

        else:
            pass
    return tweets_list_on
