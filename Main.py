from imgurpython import ImgurClient
import praw

# --- Imgur stuff ---

client_id = '4d67e81c24cc043'
client_secret = 'This goes here'
client = ImgurClient(client_id, client_secret)

# --- Reddit stuff ---

sub = 'pcmasterrace'
user_agent = ("bilbobx182crawler")
r = praw.Reddit(user_agent=user_agent)
subreddit = r.get_subreddit(sub)

# --- Meat of the Code ---

for submission in subreddit.get_new(limit=50):
    #So we don't convert too many posts in a day. Only quality stuff.

    if(submission.score < 7):
        URL = submission.url
        link = submission.url
        URL=URL.split('.')

        # So we don't attempt to convert posts that are already imgur
        if(URL[1] != 'imgur'):

            # checking to see if it ends as an image so we can try rehost it on imgur
            if(URL[-1]=='gif' or URL[-1]=='jpeg' or URL[-1]=='jpg' or URL[-1]=='png' ):
                #print("URL Ends with " + URL[-1])
                print("Uploading image... ")

                #Try and catch/except because some images that aren't on imgur can be too big to host.
                try:
                    image=client.upload_from_url(link, config=None, anon=True)
                    print("Done")
                    print(image['link'])
                except:
                    print("error occured with this image")
        else:
            print("Already an Imgur")