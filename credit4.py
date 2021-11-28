import praw
import time

reddit = praw.Reddit('bot1', user_agent='cs40')

count = 0
for submission in reddit.subreddit("Coldplay").hot(limit=300):
    a = submission.title
    b = submission.url
    reddit.subreddit('BotTown2').submit(a, url=b)
    count += 1
    print('reposted comments = ', count)
    time.sleep(5)