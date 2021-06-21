from textblob import TextBlob
import sys
import tweepy
import matplotlib.pyplot as plt


def percentage(part, whole):
    return 100 * float(part)/float(whole)


consumerKey = 'I4JIeJYX5PDmYRDp8D05uHTvw'
consumerSecret = '8E8YBZbg8q2CfdAB6VQLHPgGt0ApHWSbklars8CJePoTSJJRvH'
accessToken = '1262384577156460547-XcXM7lpaCp2um3IGVPw1mtUsCbH9as'
accessTokenSecret = 'CNxFNc3Hwncody61OX6YUAdmzCGC2wm1DWkOk9yMAABMs'

auth = tweepy.OAuthHandler(consumer_key=consumerKey,
                           consumer_secret=consumerSecret)

auth.set_access_token(accessToken, accessTokenSecret)

api = tweepy.API(auth)

sentence = input("Enter a sentence to analyze its sentiment: ")

ana = TextBlob(sentence)

h = TextBlob('Listen!')

if (ana.detect_language() != 'en'):
    ana = ana.translate(to='hi')

print(ana)


if(ana.sentiment.polarity < 0.0):
    print(-1)

elif(ana.sentiment.polarity == 0.0):
    print(0)

elif(ana.sentiment.polarity > 0.0):
    print(1)


searchTerm = input("Enter Keyword/hashtag to search about: ")
noOfSearchTerms = int(input("Enter how many tweets to analyze: "))

tweets = tweepy.Cursor(api.search, q=searchTerm).items(noOfSearchTerms)


positive = 0
negative = 0
neutral = 0
polarity = 0


for tweet in tweets:
    # print(tweet.text)
    analysis = TextBlob(tweet.text)

    polarity += analysis.sentiment.polarity

    if(analysis.sentiment.polarity == 0):
        neutral += 1

    elif(analysis.sentiment.polarity < 0.00):
        negative += 1

    elif(analysis.sentiment.polarity > 0.00):
        positive += 1


positive = percentage(positive, noOfSearchTerms)

negative = percentage(negative, noOfSearchTerms)

neutral = percentage(neutral, noOfSearchTerms)

polarity = percentage(polarity, noOfSearchTerms)

positive = format(positive, '.2f')
neutral = format(neutral, '.2f')
negative = format(negative, '.2f')


print("How people are reacting on " + searchTerm +
      " by analyzing "+str(noOfSearchTerms) + " Tweets.")

if(polarity == 0):
    print("Neutral")
elif(polarity < 0.00):
    print("Negative")
elif(polarity > 0.00):
    print("Positve")


labels = ['Positive ['+str(positive)+'%]', 'Neutral [' +
          str(neutral)+'%]', 'Negative['+str(negative)+'%]']

sizes = [positive, neutral, negative]

colors = ['green', 'blue', 'red']

patches, texts = plt.pie(sizes, colors=colors, startangle=90)

plt.legend(patches, labels, loc="best")

plt.title('How people are reacting on ' + searchTerm +
          ' by analyzing '+str(noOfSearchTerms) + ' Tweets.')

plt.axis('equal')
plt.tight_layout()
plt.show()
