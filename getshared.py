#!/usr/bin/env python
# Author : Linggar Primahastoko
# 2011 July

import re
import urllib2
import sys
import urlgrabber
import urlgrabber.progress

howto = "4shared download script\nUsage: python getshared.py http://link4shared FileName"

def proses():
	# link pertama
	link = sys.argv[1]
	buka = urllib2.urlopen(link)
	cari = re.compile('a href="(.*)"   class="dbtn"')
	dapat = re.findall(cari,buka.read())

	# link download
	baru = urllib2.urlopen(dapat[0])
	lagi = re.compile('var flvLink = \'(.*)\'')
	final = re.findall(lagi,baru.read())

	prog = urlgrabber.progress.text_progress_meter()
	urlgrabber.urlgrab(final[0],sys.argv[2],progress_obj=prog)

def main():
        if len(sys.argv) <=1:
                print howto
                sys.exit(1)
        else:
                proses()

if __name__ == "__main__":
	main()
