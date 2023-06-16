# Install the instagrapi library if not already installed
# pip install instagrapi

import concurrent.futures
from instagrapi import Client

# Set up authentication credentials
username = 'username'
password = 'password'

# Create an instance of the Client class
client = Client()

# Login to Instagram
client.login(username, password)

# Get your followers and following
followers = client.user_followers(client.user_id_from_username(username))
following = client.user_following(client.user_id_from_username(username))

# Function to retrieve user information
def get_user_info(user_id):
    user_info = client.user_info(user_id)
    return user_info.username

# Retrieve user information using multi-threading
with concurrent.futures.ThreadPoolExecutor() as executor:
    non_followers = [user_id for user_id in following if user_id not in followers]
    results = executor.map(get_user_info, non_followers)

# Print the usernames of non-followers
for username in results:
    print(username)
