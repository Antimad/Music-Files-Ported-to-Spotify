#! Python3
# Read .csv file of music
from datetime import datetime
startTime = datetime.now()
import re, csv, json,requests, sys, spotipy, spotipy.util as util,difflib
file = open('csvmsdos.csv')
filereader = csv.reader(file)
text_data = list(filereader)
# loop to append the song and artist to two lists
x = 1
songname = []
songname_list = []
songartist_list = []

for x in range(300):
    songname = text_data[x][0].split(';')
    if '(' or ')' in songname[0]:
        songname[0]= songname[0].replace('(' or ')','')
    # creation of list of artists
    
    if songname[0] == '':
        pass
    else:
        songname_list.append(songname[0])
    if songname[1] == '':
        pass
    else:
        songartist_list.append(songname[1])
    
tally = 0
group = 0
spotify_track_list = []
scope = 'user-library-read'
username='David Nwaege'
token = util.prompt_for_user_token(username,scope)
if token:
    sp = spotipy.Spotify(auth=token)
    while tally%50 == 0:
        results=sp.current_user_saved_tracks(limit =50, offset=group)
        for item in results['items']:
            track = item['track']
            spotify_track_list.append(track['name'])
            tally +=1
        group +=50        
else:
    print('failed :(')
    sys.exit()

# Retrieve list of saved songs from spotify
print (tally)
sixty_list = []
new_sixty = []
empty = 0
rejects = []
answer=[]
fanswer=[]
spotify = spotipy.Spotify()
for a in range(len(songname_list)):
    sixty_per_match = difflib.get_close_matches(songname_list[a],spotify_track_list,n=1,cutoff=0.6)
   # if not sixty_per_match:
   #     pass
    #if difflib.get_close_matches(songname_list[a],spotify_track_list,n=1,cutoff=0.7):
     #   rejects.append(songname_list)
   # else:
    new_sixty.append(sixty_per_match)
    if new_sixty[a] == '':
        new_sixty[a].remove([])
q = new_sixty[0]
results = spotify.search(q,limit=3,offset=0,type='track',market=None)
#for x in range(len(rejects)):
 #   answer = spotipy.Spotify().search(rejects[x])
  #  fanswer.append(answer)
#print (fanswer)
#print(new_sixty)
print (results)


# print (new_sixty)
# print ('it took ' + str(datetime.now() -startTime) + ' seconds to execute')

# user_playlist_create(username,'Nostalgia-list',public=True)

