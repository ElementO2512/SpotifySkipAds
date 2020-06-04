import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
from time import sleep

os.environ["SPOTIPY_CLIENT_ID"] = "688545512c0941e0be43e0ca840bd116"
os.environ["SPOTIPY_CLIENT_SECRET"] = "49205b6a5f8946e8835d2596d5d7418c"
client_credentials_manager = SpotifyClientCredentials(client_id='688545512c0941e0be43e0ca840bd116', client_secret='49205b6a5f8946e8835d2596d5d7418c')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

username = ""
scope = 'user-read-playback-state, user-modify-playback-state'
token = util.prompt_for_user_token(username, scope, redirect_uri="http://localhost:9090")

if token:
    sp = spotipy.Spotify(auth=token)
else:
    print("Can't get token for", username)

while True:
    if 1==1:
        songinfo = sp.current_playback(market=None)
        if songinfo == None:
            continue
        songinfofile = open("songinfo.txt", "w")
        songinfofile.write(str(songinfo))
        sleep(1)
        print('ok')
#while True:
#    if "ad" in songinfo:
#        sp.next_track()
#        print('Ad Skipped')
#        sleep(1)
#    else:
#        print('No Ad')
#        sleep(1)