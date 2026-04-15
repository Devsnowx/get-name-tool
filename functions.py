#! /usr/bin/python3 

('''import modules
import socket
import sys

#define function
def scanner(target,port, timeout=3):
	sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	socket.timeout(timeout)
	sock=socket.connect(target, int(port))
	sock.exit()
	
	return scanner
	
print(f")
''')

firstname=input('Enter your first legal name  : ')

lastname=input("Enter your surname(last name) : ") 
def name(firstname, lastname):
	return {firstname + "  " + lastname}
fullname=name(firstname,lastname)
print(f"fullname", fullname)	
	
