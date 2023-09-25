# Import the Twilio Python library
from twilio.rest import Client

# Your Twilio Account SID and Auth Token
account_sid = 'YOUR_ACCOUNT_SID'
auth_token = 'YOUR_AUTH_TOKEN'

# Create a Twilio client
client = Client(account_sid, auth_token)

# Your Twilio phone number and the recipient's phone number
from_number = 'YOUR_TWILIO_PHONE_NUMBER'
to_number = '+1234567890'  # Replace with the recipient's phone number

# The message you want to send
message = 'Hello, this is a test message from your Python program!'

# Send the SMS
client.messages.create(
    to=to_number,
    from_=from_number,
    body=message
)

print(f"Message sent to {to_number}: {message}")
