#!/usr/bin/env python
#Scott Hill
#ECE 442
#Mastery Challenge
#Security L1

#dependenceies
import os
import time
import random
from os.path import  isfile


sample_data = "./sample_data.txt"

original_data = ""
decoded_data = ""
encoded_data = ""
keys = []
random.seed()
randint = random.randint(0, 9)
itr = 0

#dummy string
sample_string = "This is extremely important data abcdefghijklmnopqrstuvwxyz!!"

#if the sample text file is in directory, use this.
if isfile(sample_data):
    with open(sample_data, "r+") as f:
	#iterate through each line in file
	for line in f:
	    #encode each character
	    for ch in xrange(len(line)):
		#record original data
		original_data += line[ch]
		#get random number and record in key array
		random.seed()
		randint = random.randint(0, 2000)
		keys.append(int(randint))
		#encode character in new string
		encoded_data += str(chr((ord(line[ch]) + (randint)) % 256))


	print "\nOriginal data from sample_data.txt: \n"			
	print original_data

	print "\nEncoded data from sample_data.txt: \n"
	print encoded_data

	#decode string
	for ch in xrange(len(encoded_data)):
	    decoded_data += str(chr((ord(encoded_data[ch]) - (keys[ch])) % 256))

	print "\nDecoded data from sample_data.txt: \n"
	print decoded_data
	print "\n"

#otherwise use sample string
else:
	#encode each character
	for ch in xrange(len(sample_string)):
	    #record original data
	    original_data += sample_string[ch]
	    #get random number and record in key array
	    random.seed()
	    randint = random.randint(0, 2000)
	    keys.append(int(randint))
	    #encode character in new string
	    encoded_data += str(chr((ord(sample_string[ch]) + (randint)) % 256))


	print "\nOriginal data from sample string: \n"			
	print original_data

	print "\nEncoded data from sample string: \n"
	print encoded_data

	#decode string
	for ch in xrange(len(encoded_data)):
	    decoded_data += str(chr((ord(encoded_data[ch]) - (keys[ch])) % 256))

	print "\nDecoded data from sample string: \n"
	print decoded_data



