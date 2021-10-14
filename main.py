import praw
import pickle
import simpletransformers

# initialize with appropriate values
client_id = "iwYTnsThxTEbXYDei3iXsg"
client_secret = "BMDSAPCsJDJnD8Cu1RzYovke1D5ngA"
username = "huemewpew"
password = "Morbona2@loveart"
user_agent = "AntiHateIndia by u/huemewpew"

# creating an authorized reddit instance
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     username=username,
                     password=password,
                     user_agent=user_agent)

# the subreddit where the bot is to be live on
target_sub = "indianhatespeechtest"
subreddit = reddit.subreddit(target_sub)

# phrase to trigger the bot
#trigger_phrase = "! NoMoreHate"

# enchant dictionary
filename = 'model.pkl'
model = pickle.load(open(filename, 'rb'))

# check every comment in the subreddit
for comment in subreddit.stream.comments():
    #comment.reply("Ye bot comment hai")
    prediction, raw_output = model.predict([comment.body])
    if(prediction == 1):
        comment.reply("@" + comment.author + "Your comment is deleted as it is detected as hate speech. Please respect your fellow users.")
        comment.delete

