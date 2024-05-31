import os
import time
import pygame


pygame.init()
pygame.mixer.init()


sound = pygame.mixer.Sound('audio.wav.wav')


def pause():
    pygame.mixer.pause()

def play():
    sound.play()  
    while True:
        stop_playback = input("Press S to stop the playback and go back to the menu: ")
        if stop_playback.upper() == 'S':  
            pause()
            return 
        else:
            continue    


while True:
    os.system("cls")  
    print("Music Player")
    time.sleep(1)
    print("Press P to play and S to pause")
    print("Press any other key to exit the music player ")
    userInput = input().upper()  
    
    if userInput == 'P':
        print("Playing music...")
        play()
    elif userInput == 'S':
        pause()
    else:
        break  
