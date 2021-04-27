import win32com.client
import win32gui
import time
import os
import sys
import pyautogui as keyboard  # pour simuler un clavier



arrayforth = "colorForth"  # nom de la fenetre  !

cheminarrayforth = "C:/GreenArrays/EVB002"
programme_arrayforth = "Okad.bat"

shell = win32com.client.Dispatch("WScript.Shell")


os.chdir(cheminarrayforth) # on se place dans le repertoire arrayforth
shell.Run(programme_arrayforth) # on lance arrayforth via Okad.bat
time.sleep(2) # on attend que le programme soit bien lance

h = win32gui.FindWindow(None, arrayforth)  # handle fenetre colorforth
#win32gui.ShowWindow( h, False) # la fenetre colorforth est cachee

input ("texte : ")
print ('Hello !')
print("le texte :  " , input)
print ('Hello !')
print ('Hello !')

time.sleep(2)
# on reactive devant la fenetre colorforth
shell.SendKeys('%') # ALT Key  a ne pas oublier pour rendre active la fenetre  !
win32gui.SetForegroundWindow(h)
time.sleep(2)

texte = 'warm compile 0 !back '
keyboard.write(texte , 0.1) # on ecrit avec un delais de 100ms entre les touches
time.sleep(2)
win32gui.ShowWindow( h, True) # la fenetre colorforth est de nouveau visible
time.sleep(2)
sys.exit()





