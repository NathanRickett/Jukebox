import time, vlc, sys, os
from pathlib import Path
 

 # method to play video
def play_song():
    
    if song_loaded == True:
        player.play()
    else:
        print("no song is loaded")

def pause_song():
    if song_loaded == True:
        player.pause()
    else:
        print("no song is loaded")

def stop_song():
    if song_loaded == True:
        player.stop()
    else:
        print("no song is loaded")

def display_songs():
    source_dir = '/home/jukebox/jukebox_app/songs/registered/'
    files = os.listdir(source_dir)
    print('\n----------SONGS----------\n')
    for file in files:
        print(file)


def load_song(media):
    player.set_media(media)

       
def find_song(user_input):
    source_dir = '/home/jukebox/jukebox_app/songs/registered/'
    files = os.listdir(source_dir)
    file_choice = user_input
    if file_choice in files:
        media = vlc_instance.media_new(source_dir + file_choice)
        return media
    else:
        return None


def play_util_sound(UTIL_NUM, media):
    util_dir = '/home/jukebox/jukebox_app/songs/util/'
    if UTIL_NUM == 1:
        oof = vlc_instance.media_new(util_dir + 'oof.mp3')
        player.set_media(oof)

    elif UTIL_NUM == 2:
        success = vlc_instance.media_new(util_dir + 'success.mp3')
        player.set_media(success)

    elif UTIL_NUM == 3:
        excellent = vlc_instance.media_new(util_dir + 'excellent.mp3')
        player.set_media(excellent)
    
    player.play()
    #if the player already had media set, set it again
    if media != None:
        player.set_media(media)



vlc_instance = vlc.Instance()
player = vlc_instance.media_player_new()

#play start up sound
play_util_sound(3, None)

song_loaded = False
current_song_media = None
current_song_name = None
last_input = None

#attempt to load a song before doing anything
while song_loaded == False:
    display_songs()
    user_input = input()
    if user_input != last_input:
        last_input = user_input
        media = find_song(user_input)
        if media != None:
            play_util_sound(2, media)
            load_song(media)
            song_loaded = True
            play_song()
            current_song_name = user_input
            current_song_media = media
        else:
            print("\nUnable to find a song using the input: " + user_input)
            play_util_sound(1, None)

print('Play: 1\nPause: 2\nStop: 3\nLoad Song Name: : All other input \n')

#get user input
while True:
    user_input = input()
    if user_input == '1':
        play_song()
    elif user_input == '2':
        pause_song()
    elif user_input == '3':
        stop_song()
    else:
        if user_input != current_song_name:
            stop_song()
            media = find_song(user_input)
            if media != None:
                play_util_sound(2, current_song_media)
                load_song(media)
                play_song()
                current_song_name = user_input
                current_song_media = media
            else:
                print("unable to find song with input " + user_input)
                play_util_sound(1, current_song_media)




