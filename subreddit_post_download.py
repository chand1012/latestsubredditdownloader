import praw
from json import loads

def json_extract(thing='', filename='data.json'):
    json_file = open(filename)
    json_data = loads(json_file.read())
    json_file.close()
    if not thing is '':
        return json_data[thing]
    else:
        return json_data

#reddit = praw.Reddit(client_id=json_extract('client_id'), client_secret=json_extract('client_secret'), password=json_extract('password'), user_agent=json_extract('user_agent'), username=json_extract('username'))
reddit = praw.Reddit(client_id=json_extract('client_id'), client_secret=json_extract('client_secret'), user_agent=json_extract('user_agent'))

try:
    print('Logged in as {}\n'.format(reddit.user.me()))
except:
    print('Logged in as Reddit\n')

subreddit = input("Enter subreddit to extract from:")
limit = int(input("Enter number of posts to extract:"))
for submission in reddit.subreddit(subreddit).hot(limit=limit):
    print(submission.title)  # Output: the submission's title
    print(submission.score)  # Output: the submission's score
    print(submission.id)     # Output: the submission's ID
    print(submission.url)    # Output: the URL the submission points to
                            # or the submission's URL if it's a self post
    subreddit_file = open('subreddit.txt', 'a')
    subreddit.write(submission.title)
    subreddit.write(submission.score)
    subreddit.write(submission.id)
    subreddit.write(submission.url)
    subreddit_file.close()
