import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

import tweepy
import requests

client = tweepy.Client( bearer_token=os.getenv('bearertoken'),
                        consumer_key=os.getenv('consumer_key'),
                        consumer_secret=os.getenv('consumer_secret'),
                        access_token=os.getenv('access_token'),
                        access_token_secret=os.getenv('access_token_secret'),
                        return_type=requests.Response,
                        wait_on_rate_limit=True)                        


query = '#100daysofcode (pandas OR python) -is:retweet'


tweets=client.search_recent_tweets(query=query,tweet_fields=['author_id','created_at','lang'],max_results=100)
tweets_json=tweets.json()
#print(tweets_json)

tweets_data=tweets_json['data']
df=pd.json_normalize(tweets_data)
#print(df)
df.to_csv('data/tweets.csv')


#import re
import re

#define your function here
def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)

    if match:
        return True
    return False

# Initialize list to store tweet counts
[pandas, python] = [0, 0]

# Iterate through df, counting the number of tweets in which each(pandas and python) is mentioned.
for index, row in df.iterrows():
    pandas += word_in_text('pandas', row['text'])
    python += word_in_text('python', row['text'])

df = pd.DataFrame([pandas, python])

# Import packages
import matplotlib.pyplot as plt
import seaborn as sns

# Set seaborn style
sns.set(color_codes=True)

# Create a list of labels:cd
cd = ['pandas', 'python']

# Plot the bar chart
ax = sns.barplot( data = df)
#ax = sns.barplot(cd, [pandas, python])
ax.set(ylabel="count")
ax.set(xlabel=cd)
plt.show()

#df.plot.bar(title="Conteo en Tweets")