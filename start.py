# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import time
import sys

running = True
while running and time.localtime(4) == (0,30):
# local.time index "4" is the minute mark
# Uses Twilio to send a text message using their API
    def send_msg(msg):
    # Your Account Sid and Auth Token from twilio.com/console
        account_sid = 'ACeecbc7f2c2329a5b2f86bd9be847e3c0'
        auth_token = '5fb1c0e0af7ddc84b88aae091b91abf7'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
                                    body=msg,"30 min study text"
                                    from_="+19124212491",
                                    to="+19126635271"
                                    )

time.sleep(60)

# 1. Loop continuously
# 2. Look at the time and see if it's time to send SMS
# 3. Send SMS message telling me to start studying
#
# Things you will need:
# Functions, Loops, Conditions, Variables, Library (twilio)
# Use import time to read the time
# Use sleep to wait 1 minute between each loop cycle
#
# git add filename
# git commit -m "message"
# git push origin master
