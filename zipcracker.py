from zipfile import ZipFile
import argparse

parser = argparse.ArgumentParser(description="\nUsage: python3 zipcracker.py -z <zipfile.zip> -p <wordlist>")
parser.add_argument("-z", dest="ziparchive", help="zip archive file")
parser.add_argument("-p", dest="wordlist", help="wordlist file to be included")
parsed_args = parser.parse_args()

try:
	ziparchive = ZipFile(parsed_args.ziparchive)
	wordlist = parsed_args.wordlist
	foundpass = ""
	
except:
	print(parser.description)
	exit(0)
	
with open(wordlist, "r") as f:
	for line in f:
		password = line.strip("\n")
		password = password.encode("utf-8")
		
		try:
			foundpass = ziparchive.extractall(pwd=password)
			if foundpass is None:
				print("Password is correct", password.decode())
		except RuntimeError:
			pass
			
	if foundpass == "":
		print("Password is not found")

			