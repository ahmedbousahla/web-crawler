
import tweepy

consumer_key = input('input your consumer key')
consumer_secret = input('input your consumer secret')
access_token =input( 'input your access token')
access_secret = input('input your access secret')
tweetsPerQry = 100
maxTweets = 1000000
hashtag = "#algeria"

authentication = tweepy.OAuthHandler(consumer_key, consumer_secret)
authentication.set_access_token(access_token, access_secret)
api = tweepy.API(authentication, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
maxId = -1
tweetCount = 0
while tweetCount < maxTweets:
	if(maxId <= 0):
		newTweets = api.search(q=hashtag, count=tweetsPerQry, result_type="recent", tweet_mode="extended")
	else:
		newTweets = api.search(q=hashtag, count=tweetsPerQry, max_id=str(maxId - 1), result_type="recent", tweet_mode="extended")

	if not newTweets:
		print("No More Tweet :(")
		break
	
	for tweet in newTweets:
		print(tweet.full_text.encode('utf-8'))
		
	tweetCount += len(newTweets)	
	maxId = newTweets[-1].id
