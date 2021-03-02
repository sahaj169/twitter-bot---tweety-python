import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user.api.me()


def limit_handle(cursor):
	try:
		while True:
			yield cousor.next()
	except tweepy.RateLimitError:
		time.sleep(300)


search_string = 'python'
numberOfTweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
	try:
		tweet.favorite()
		#tweet.retweet()
		print('I liked that tweet')
	except tweepy.TweepError as e:
		print(e.reason)
	except StopIteration:
		break






# #genrous Bot
# for follower in limit_handler(tweepy.Cursor(api.followers).items()) :
# 	if follower.name=='#name of the person you wanted to follow':
# 		#follower.followers_count >100 : we can use diff. conditions here
# 		follower.follow()
# 		break
	






































# import tweepy

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)

# api = tweepy.API(auth)
# user= api.me()
# print(user.screen_name)
# print(user.follower_count)