#!/usr/bin/python
import twitter,time,simplejson,urllib

def get_followers(screenName,cursorPos='-1'):

  url="http://api.twitter.com/1/statuses/followers/%s.json?cursor=%s" % (screenName,cursorPos)
  print "in get_followers() cursorPos is :%s" % (cursorPos)
  result=simplejson.load(urllib.urlopen(url))
  entries=result['users']
  return entries, result['next_cursor_str']


def getUserInfo(user):
  userinfo={}
client = twitter.Api(username='neilkod2',password='demopassword')
flom=client.GetUser(uid)


name,tweets,followers,pct = ParseUser(user)
i=0
nextCursor = "-1"
uid='peterflom'
file='%s_followers.txt' % (uid)
fileHandle = open(file,'w')
print "start: nextCursor is %s" % (nextCursor)

while nextCursor <> "0":
  print "iteration 0 begin: nextCursor: %s" % (nextCursor)
  followers,nextCursor = get_followers(uid,nextCursor)
  print nextCursor
  i=i+1

  # write to a log

  for ff in followers:
    name = ff['screen_name']
    tweets = ff['statuses_count']
    followers = ff['followers_count']
    pct = float(tweets) / float(followers)
    text="%s\t%s\t%s\t%f" % (name, tweets,followers,pct)
    fileHandle.write(text + '\n')


fileHandle.close()

"""  
client = twitter.Api(username='neilkod2',password='demopassword')
uid = 'peterflom'
flom=client.GetUser(uid)
myFriends = flom.GetFriendsCount()
myTweets = flom.GetStatusesCount()
pct = float(myTweets)/float(myFriends)
#pages = myFriends/100
print "my screen name: %s" % (uid)
print "my friend count: %s" % (myFriends)
print "my tweet count: %s" % (myTweets)
print "my tweet/follower ratio: %f" % pct
print "user\ttweets\tfollowers\tpct"
for pageNum in range(1,5):
  print "pageNum is: %s " % (pageNum)
  followers=client.GetFriends(uid,page=pageNum)
  time.sleep(1.5)

  for ff in followers:
	  name = ff.GetScreenName()
	  tweets = ff.GetStatusesCount()
	  followers = ff.GetFriendsCount()
	  pct = float(tweets) / float(followers)
	  print "%s\t%s\t%s\t%f" % (name, tweets,followers,pct)

"""