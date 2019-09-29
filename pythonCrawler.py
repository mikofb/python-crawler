"""
	A small crawler for retrieving links from a given URL.
	It goes throught an URL and returns	all the links found there.
	
	[Requires]:
				- Python3
				- BeautifulSoup from bs4 module which has been inclued in the Files directory.

	[Author]:	Mikofb at https://github.com/mikofb
	[Licence]: MIT
"""
import sys
import urllib

if sys.version_info[0] == 3:
    from urllib.request import urlopen
else:
    from urllib import urlopen

from bs4 import BeautifulSoup

links = []

def main():
	print("#------------------------------#")
	print("#--------PYTHON CRAWLER--------#")
	print("#------------------------------#\n")
	url = input("$> URL [http(s)://www.example.com]: ")
	print("$> Crawling...")
	try:
		r 	= urllib.request.urlopen(url)
		soup = BeautifulSoup(r.read(),"lxml")
		for link in soup.find_all('a'):
			try:
				links.append(link['href'])
				current_link = link.get('href')
				try:
					try:
						if current_link.endswith('pdf'):
							print('[pdf]: {}'.format(link.get('href')))
						elif current_link.endswith('php'):
							print('[php]: {}'.format(link.get('href')))
						elif current_link.endswith('doc'):
							print('[word]: {}'.format(link.get('href')))
						elif current_link.endswith('mp4'):
							print('[moovie]: {}'.format(link.get('href')))
						else:
							print('[link]: {}'.format(link.get('href')))
					
					except AttributeError:
						raise
				except UnicodeEncodeError:
					pass
			except KeyError:
				pass
		print("\n")
		print("$> URL: {} ".format(url))
		print("$> Links: {}".format(len(links)))
		print("$> End")
	except:
		print('$> Please try again')		

if __name__ == '__main__':
	main()