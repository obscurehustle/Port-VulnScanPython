#!/usr/bin/python

import  socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "192.168.1.254"
port =  221

def portScanner(port):
	if sock.connect_ex((host, port)):
		print ("Port %d is closed" % (port))
	else:
		print ("Port %d is opened" % (port))

portScanner(port)
