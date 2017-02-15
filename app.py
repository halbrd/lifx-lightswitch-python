import json
from pifx import PIFX

token = json.load(open('token.json', 'r'))["token"]

p = PIFX(token)

p.toggle_power()
