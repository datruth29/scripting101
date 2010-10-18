#!/usr/bin/env python

import sys

sout = sys.stdout
#Move standout to file output.txt
sys.stdout = open('output.txt', 'w')
print "This is a file, receiving standard output."

#Now were closing the file, and setting the standard out back to display
sys.stdout.close
sys.stdout = sout

#Now, lets re-open the file, but with an Exception, to make sure it exists

try:
    thisfile = open('dutput.txt', 'r')
except IOError:
    print "This file does not exist, something went wrong."
else:
    print "The file was read correctly, here are the contents. :"
    soutContent = thisfile.read()
    print soutContent
    thisfile.close

#ValueError Exception
while True:
    try:
        x = int(raw_input("Please enter a number: "))
        if x==0:
            break
    except ValueError:
        print "Oops! That was no valid number. Try again..."
