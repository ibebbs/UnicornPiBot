import sys
import random

from UHScroll import *
from twython import TwythonStreamer
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

colours = ['red','white','pink','blue','green','cyan']

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

class UnicornPiBotStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            text = data['text'].translate(non_bmp_map)
            colour = random.choice(colours)
            print(text)
            unicorn_scroll(text, colour, 200, 0.05)

stream = UnicornPiBotStreamer(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

stream.statuses.filter(track='#INWED17')
