import requests
import time

def fetch_submissions(keyword, size=100, before=None, after=None):
    url = f"https://api.pushshift.io/reddit/search/submission/?q={keyword}&size={size}"
    if before:
        url += f"&before={before}"
    if after:
        url += f"&after={after}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['data']
    else:
        return None

def fetch_comments(keyword, size=100, before=None, after=None):
    url = f"https://api.pushshift.io/reddit/search/comment/?q={keyword}&size={size}"
    if before:
        url += f"&before={before}"
    if after:
        url += f"&after={after}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['data']
    else:
        return None

def fetch_data_with_retries(url, retries=3, delay=5):
    for _ in range(retries):
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        time.sleep(delay)
    return None

def fetch_reddit_data(keyword, size=100, before=None, after=None):
    submissions = fetch_submissions(keyword, size, before, after)
    comments = fetch_comments(keyword, size, before, after)
    return submissions, comments

# Parameters
keyword = 'Israel Palestine conflict'
size = 100  # Number of results to fetch
before = None  # Unix timestamp (optional)
after = None   # Unix timestamp (optional)

submissions, comments = fetch_reddit_data(keyword, size, before, after)

# Print Submissions
print("Submissions:\n")
if submissions:
    for submission in submissions:
        print(f"Title: {submission['title']}")
        print(f"Author: {submission['author']}")
        print(f"Created UTC: {submission['created_utc']}")
        print(f"URL: {submission['url']}\n")
else:
    print("No submissions found.")

# Print Comments
print("Comments:\n")
if comments:
    for comment in comments:
        print(f"Author: {comment['author']}")
        print(f"Comment: {comment['body']}")
        print(f"Created UTC: {comment['created_utc']}\n")
else:
    print("No comments found.")