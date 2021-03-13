#!/bin/python3

import sys
import socket
from datetime import datetime

#define our target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #translate hostname to ipv4
else:
	print("invalid amounts of arguments.")
	print("syntax: python3 scanner.py <ip>")

#add a pretty banner
print("-" * 5)
print("scanning target "+target)
print("time started: "+str(datetime.now()))
print("-" * 5)

try:
	for port in range(50,85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port)) #returns an error indicator
		if result == 0:
			print("port {} is open".format(port))
		s.close()
except KeyboardInterrupt: #hit ctrl+c exit the program
	print("\nExiting program.")
	sys.exit()
except socket.gaierror:
	print("Hostname couldn't be resolved.")
	sys.exit()
except socket.error:
	print("Couldn't connect to server.")
	sys.exit()
