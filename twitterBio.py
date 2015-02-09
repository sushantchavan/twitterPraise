import tweepy
import csv

consumer_key = 'R3ZXuqiuST9jhJOBeL9yT8K23'
consumer_secret = 'mzpQLTLVB2BPeGu7VbMTJNwu18GK9gBWFCXwTtMsKA0tf9IgiC'
access_token = '2605251686-Tm9RtMd9qxSGZVpyvPo5i3p3ZLIwdLAQ2EtiGiM'
access_token_secret = 'm3zJpM35ML2O6dBYDSivQ1Hxne83UHMtLAVR6V4xoFp3X' 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

list = ['@jmsidhu', '@dekrey','@MarketsforGood','@drivendataorg'
,'@zerodie'
,'@DataKind'
,'@inthecompanyof'
,'@GarfieldFisher'
,'@SenorG'
,'@yochum'
,'@AlexKotyck'
,'@LoraineLawson'
,'@p2173'
,'@boonrs'
,'@AlonHalevy'
,'@aric_chokey'
,'@thanyawzinmin'
,'@kaythaney'
]

users = []

api = tweepy.API(auth)

with open('result.csv', 'wb') as csvfile:
	result = csv.writer(csvfile)
	for screenName in list:
		user = api.get_user(screenName)
		user.screen_name = user.screen_name.encode('utf-8')
		user.name = user.name.encode('utf-8')
		user.location = user.location.encode('utf-8')
		user.description = user.description.encode('utf-8')
		user.profile_image_url = user.profile_image_url.encode('utf-8')
		user.profile_background_image_url = user.profile_background_image_url.encode('utf-8')

		#print user.name
		#print user.location
		#print user.description
		#print user.profile_image_url
		#print user.profile_background_image_url

		result.writerow([user.screen_name,user.name,user.location,user.description,user.profile_image_url,user.profile_background_image_url])