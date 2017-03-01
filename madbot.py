import praw
import pdb
import re
import os
import time

#Requires a praw bot to be set up
r = praw.Reddit('bot1')

USERNAME = "YourUsernameHere" #Change this to your username obviously

#Change the subreddit if you like
subreddit = r.subreddit("drama")

index = 0

data = ["Try going for a jog! That might help you get all that built-up madness out of your system.",
        "You could listen to music. Lots of people listen to music when they're mad. ",
        "Have you visited a doctor? He might be able to tell you why you're so mad. ",
        "Have you had enough sleep? If you haven't gotten enough sleep, you might find yourself making yourself mad.",
        "Have you had any food to eat? If you haven't taken care of your body, that might make you mad. ",
        "All you have to do is be happy for a little while, and you'll forget madness. Try going outside! ",
        "I know you might think you have a good reason for being mad. But you're still mad. ",
        "Try being happy. Just for a day. You'll never want to be mad again. ",
        "Maybe so. But at the end of the day, I'll sleep soundly, and you'll still be mad. ",
        "Did someone tell you that being mad is what happiness feels like? Because if so, you should try being happy and you'll never want to be mad again. ",
        "At the end of your life, do you want to be remembered as a great creator, a good friend, a wonderful person, a sterling example? Or do you want to be forgotten because you spent your life mad? ",
        "If you let being mad control you, all you'll have left is being mad. ",
        "I know being mad makes it feel like you can't be anything but mad, but all you have to do is stop being mad. ",
        "You sound mad. Thanks for letting us know!",
        "You don't have to be mad anymore! ",
        "How many minutes - days - years of your life have you spent being mad, instead of happy? ",
        "If being on the Internet makes you this mad, you should know that at any moment you could put the computer away, go outside, and be happy for the rest of your life. ",
        "Every minute you spend being mad is a minute you could have been happy instead. ",
        "Your friends don't want you to be mad, you know. Try being happy, for their sake!",
        "https://www.youtube.com/watch?v=T8kt22TH_c4",
        "https://www.youtube.com/watch?v=lhF8iDJIM_M",
        "When people run in circles, it's a very very mad world. Or in your case, a very angry Redditor!",
        "https://www.youtube.com/watch?v=bnam9hljQDQ"] #Add your own auto-replies if you want

if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "r") as f:
       posts_replied_to = f.read()
       posts_replied_to = posts_replied_to.split("\n")
       posts_replied_to = list(filter(None, posts_replied_to))

print "Start!\n"
print "Excluded comments: " + str(posts_replied_to)

while(1==1):
    try:
        for comment in subreddit.stream.comments():
            print comment.body + "\n"
            if comment.id not in posts_replied_to and comment.author != USERNAME and  ((comment.parent().author == USERNAME) or (comment.submission.author == USERNAME)):
                c = data[index]
                posts_replied_to.append(comment.id)
                print "Going to reply to " + str(comment.author) + " with '" + c + "' in 10 seconds\n"
                print "Comment replying to:\n"
                print str(comment.body) + "\n"
                with open("posts_replied_to.txt", "w") as f:
                     for post_id in posts_replied_to:
                        f.write(post_id + "\n")
                time.sleep(10)
                comment.reply(data[index])
                print "Replied to comment"
                if(index >= len(data)-1):
                    index = 0
                else:
                    index += 1               
    except:
        print "Lost connection to stream. Re-connecting in 10..."
        time.sleep(10)
