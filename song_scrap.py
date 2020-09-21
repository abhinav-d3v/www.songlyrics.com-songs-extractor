from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import string,random
path = "C:\chromedriver.exe"

def save_to_file(filename, lyrics):
	# if not os.path.exists(path):
	# 	os.mkdir('Metallica')
	if os.path.exists('Metallica') == False:
		os.mkdir('Metallica')
	if 'Lyrics' in filename:
		filename = filename.replace('Lyrics', '')
		filename = filename.replace('?', '')
		filename = filename.strip()
	f = open("Metallica/" + filename + ".txt", "w")
	try:
		f.write(lyrics)
	except:
		print(lyrics)
	f.close()
def read_file():
	filename = os.listdir('Metallica')
	songs = {}
	# all songs name with their Lyrics are saved in dict
	for file in filename:
		f = open('Metallica/' + file, 'r')
		songs[file.replace('.txt', '').strip()] = f.read()

driver = webdriver.Chrome(path)
driver.get("http://www.songlyrics.com/metallica-lyrics/")
# find songs in box css
box_of_song = driver.find_elements(By.CLASS_NAME, 'listbox')
# finding element with song a tag
songs_list = box_of_song[0].find_elements(By.TAG_NAME, 'a')
songs_link = []
for song in songs_list:
	# extracting link value
	songs_link.append(song.get_attribute('href'))
for link in songs_link:
	# link = 'http://www.songlyrics.com/metallica/the-unforgiven-ii-lyrics/'
	driver.get(link)
	song_name = WebDriverWait(driver,10).until(lambda d: d.find_elements(By.TAG_NAME, 'h1'))
	# song_name = driver.find_elements(By.TAG_NAME, 'H1')
	song_title = song_name[0].text
	lyrics_songs = driver.find_elements(By.ID, 'songLyricsDiv')
	for lyrics in lyrics_songs:
		save_to_file(song_title,lyrics.text)
driver.quit()


