#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The MIT License (MIT)

Copyright (c) 2015 SourceSlayer

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

from __future__ import division
import socket
from sys import version_info, stdout
from argparse import ArgumentParser
import os
from subprocess import check_output
import time
try:
    import keyring
except ImportError:
    pass
if version_info[0]<3:
    input=raw_input

def update_console_load(completion, total):
    width=int(check_output(["tput", "cols"]))-10
    remaining=total-completion
    if width%2!=0:
        width-=1
    percentage=completion/total
    stdout.write("\r|%s%s|    %d%%" %("-"*(int(((width)*(completion/total)))), " "*(width-int(((width)*(completion/total))) if completion!=0 else 0), percentage*100))
    stdout.flush()

def get_input(query, default, password=False, instruction=False):
    entry=input("%s (%s): " %(query, default)) if instruction else input("%s [%s]: " %(query, default))
    if entry==None and not password:
        return default
    elif password and entry=="":
        return True
    return query

def get_selection(options):
    for o, i in options, len(options):
        print((i+1)+". "+o)
    return options[int(input("Choice: "))-1]

class Project:#Loaded from the Project.json file.
    def __init__(self, name, location):
        self.name=name
        self.location=location

class ServerConnection:
#    def __init__(self, host, port, username):

    def authenticate(self, username, password, host=None, port=None, server_password=None):
        """Authenticates to a serverusing the host and port information from
        that server along with the username and password. If no host and port
        are found, it will assume that your intention was to use this server."""

class PyCollab:
    def __init__(self, host, port):
        self.connection=ServerConnection()
        options={"authenticate":self.authentication_dialog, "help":self.help, "exit":exit}
        self.options=options
        while True:
            entry=input("> ").split(" ")
            print(options[entry.pop(0)](*entry) if entry[0] in options.keys() else "Error: Not an option, type \"Help\" to see available options")

    def authentication_dialog(self):
        server=get_input("Server Name", "Type an asterick (*) or period (.) to select from list")
        if server in [".", "*"]:
            selection=get_selection(["History", "Saved"])


    def help(self):
        """Shows out options for PyCollab"""
        print("Available choices to for pycollab client: ")
        for i in self.options:
            print(i+" -- "+str(self.options[i].__doc__))



if __name__=="__main__":
    parser=ArgumentParser()
    parser.add_argument("-s", "--server", help="Specifies the server and port of the connection as host:port, the option saved to the package.json file will be used if not specified.")
    parser.add_argument("-a", "--server_password", help="If the server requires a password, use this option to specify it.")
    parser.add_argument("-p", "--package", help="Sets the package.json file for the project if not found in directory.")
    parser.add_argument("-l", "--login", help="Offers option to login to server specifying server and being prompted for username and password.")
    args=parser.parse_args()
    host, port=args.server.split(":")
    if parser.get
    collab=PyCollab(host, port)
