#!/usr/bin/python
# -*- coding: utf-8 -*-
#Basic Information Gathering Tool (BigT) by rp0track
#BigT is designed to enumerate Linux operation system and identify words in files

import os
import sys
from termcolor import colored

os.system("clear")
def menu_principal():
	print colored ("Basic Information Gathering Tool (BigT)", "red")
	print "1. Enumerating Information From Linux"
	print "2. File Search and Identify Words"
	print "3. Identify Words"
	print "0. Exit"
loop = True
while loop:
	menu_principal()
	opcion = input("Choose a option: \n")
	if opcion >= 4:
		print "Incorrect option, try again..."
	elif opcion==1:
		print colored ("Enumerating Information From Linux", "red")
		EnumSO = open("EnumSO", "w")
		os.system("echo '[*]Kernel version' >> EnumSO")
		os.system("uname -an >> EnumSO")
		os.system("echo '[*]Hostname' >> EnumSO")
		os.system("cat /etc/hostname >> EnumSO")
		os.system("echo '[*]Current directory' >> EnumSO")
		os.system("pwd >> EnumSO")
		os.system("echo '[*]Users connected to the Operating System' >> EnumSO")
		os.system("w >> EnumSO")
		os.system("echo '[*]Current user' >> EnumSO")
		os.system("whoami >> EnumSO")
		os.system("echo '[*]Network Configuration' >> EnumSO")
		os.system("ifconfig >> EnumSO")
		os.system("echo '[*]Users' >> EnumSO")
		os.system("cat /etc/passwd >> EnumSO")
		os.system("echo '[*]Groups' >> EnumSO")
		os.system("cat /etc/group >> EnumSO")
		os.system("echo '[*]World Writable Directories' >> EnumSO")
		os.system("find / -xdev -type d \( -perm -0002 -a ! -perm -1000 \) -print >> EnumSO")
		os.system("echo '[*]Worl Writable Files' >> EnumSO")
		os.system("find / -perm -2 ! -type l -ls >> EnumSO")
		os.system("echo '[*]Files with Sticky Bit' >> EnumSO")
		os.system("find / -type f \( -perm -04000 -o -perm -02000 \) >> EnumSO")
		os.system("echo '[*]Shares' >> EnumSO")
		os.system("cat /etc/exports >> EnumSO")
		os.system("echo '[*]Processes' >> EnumSO")
		os.system("ps -fea >> EnumSO")
		os.system("echo '[*]Network Connections' >> EnumSO")
		os.system("netstat -a >> EnumSO")
		os.system("echo '[*]Software and version' >> EnumSO")
		os.system("rpm -qa >> EnumSO")
		os.system("dpkg --list >> EnumSO")
		print "[*]See file EnumSO"
		EnumSO.close()
		os.system("chmod 700 EnumSO")
		print colored("[*]Return to Main Menu", "red")
	elif opcion==2:
		print colored ("File Search and Identify Words", "red")
		print "Enter main path for searching..."
		path = raw_input()
		print "Enter file extensions for searching"
		print "Example: .sh .txt .ora .cnf .config .c"
		extension = raw_input()
		lista_extension = extension.split(' ')
		print "Enter words for searching in files..."
		print "Example: password user connect conn sid pass contraseña"
		palabra = raw_input()
		lista_palabra = palabra.split(' ')
		print "[*]Looking for files ..."
		for extension in lista_extension:
			print colored("[*]Looking for files with extension: \n", "red"), extension
			lisfe = open("Archivos", "a")
			for root, dirs, files in os.walk(path):
				for name in files:
					if name.endswith(extension):
						lisfe.write(os.path.join(root, name,'\n'))
		lisfe.close()
		print colored("[*]Search ended ...", "green")
		print colored("[*]Words Searching...", "green")
		listafiles = open("Archivos", "r")
		resultado = open("Resultado", "a")
		for line in listafiles:
			resultado.write("[*]" + ' ' + line)
			try:
				archivo = open(line[:-2], "r")
				for line in archivo:
					for palabra in lista_palabra:
						if palabra in line:
							resultado.write(line)
			except IOError:
				resultado.write("[-]File not found... \n")
		print "[*]See file Resultado"
		print colored("[*]Return to Main Menu", "red")
	elif opcion==3:
		print colored ("Identify Words", "red")
		print "Enter the path of file list"
		print "Example: /home/rp0track/FileList.txt"
		listado = raw_input()
		print "Enter words to find..."
		print "Example: password user connect conn sid pass contraseña"
		palabra = raw_input()
		lista_palabra = palabra.split(' ')
		print colored("[*]Words searching \n", "green")
		print lista_palabra
		listado_files = open(listado, "r")
		resultado = open("Resultado", "a")
		for line in listafiles:
			resultado.write("[*]" + ' ' + line)
			try:
				archivo = open(line[:-2], "r")
				for line in archivo:
					for palabra in lista_palabra:
						if palabra in line:
							resultado.write(line)
			except IOError:
				resultado.write("[-]File not found...\n")
		print "[*]Search ended..."
		print "[*]See file Resultado"
		print colored("[*]Return to Main Menu", "red")
	elif opcion==0:
		print "End"
		loop = False
