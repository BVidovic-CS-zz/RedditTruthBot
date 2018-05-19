import praw


#will get auth data from file
auth_file = open('/Users/bvidovic/Documents/reddit_bot_auth.txt' , 'r')

reddit = praw.Reddit(client_id=auth_file.readline().strip(),
                     client_secret=auth_file.readline().strip(),
                     password=auth_file.readline().strip(),
                     user_agent=auth_file.readline().strip(),
                     username=auth_file.readline().strip())

print(reddit.user.me())
for submission in reddit.front.hot():
    print(submission)