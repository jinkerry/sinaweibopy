# -*- coding: utf-8 -*-
__author__ = 'ChenKan'

from weibo import APIClient

APP_KEY = 'THE_KEY'
APP_SECRET = 'THE_SECRET'
CALLBACK_URL = 'http://chenkan.github.io'

client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
url = client.get_authorize_url()
print url   # Open the url and get the code

SOME_CODE = 'THE_CODE'
r = client.request_access_token(SOME_CODE)
access_token = r.access_token
expires_in = r.expires_in
client.set_access_token(access_token, expires_in)

print client.statuses.user_timeline.get()
print client.statuses.update.post(status=u'HAVE A POST')
