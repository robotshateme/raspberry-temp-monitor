# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC6dffa441aa4d6f12b6fb178cd69edb51"
auth_token = "28f10c53564693007be6264495643ca0"
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hello there!',
                              from_='+16162192987',
                              to='+12693120639'
                          )

print(message.sid)
