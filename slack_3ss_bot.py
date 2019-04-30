from slacker import Slacker
import json
# import argparse
# import os

person_dict = {
    "U7M96QQ4D": "Kevin",
    "U9C2JDSNQ": "Peter",
    "U5W1TB7T6": "Veena",
    "UCLH6P71P": "Curtis",
    "U7RJSQLHF": "Beau",
    "U90EGHGAJ": "Catherine",
    "UBCV654U8": "Selena"
}

token = 'xoxp-4307037491-306492594358-602477360578-cf19826bb64a7eed5ed174a05fa9a26b'

slack = Slacker(token)
channels = slack.channels.list().body['channels']
# print(channels)

dstand_id = "CB5SHNCHK"

channel_history = slack.channels.history(dstand_id, count=10).body['messages']
for message in channel_history:
    if message["text"].lower().startswith("3ss"):
        print(f"{person_dict[message['user']]}: {message['text']}")
        print("\n")
# messages = getHistory(slack.groups, group['id'])