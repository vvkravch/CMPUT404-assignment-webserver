#  coding: utf-8 
import socketserver
import cgitb
cgitb.enable()

# Copyright 2013 Abram Hindle, Eddie Antonio Santos
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#
# Furthermore it is derived from the Python documentation examples thus
# some of the code is Copyright © 2001-2013 Python Software
# Foundation; All Rights Reserved
#
# http://docs.python.org/2/library/socketserver.html
#
# run: python freetests.py

# try: curl -v -X GET http://127.0.0.1:8080/
import os


def directoryContents ():
    #use www from current direcotry
    path = "./www"
    contents=os.listdir(path)
    
    return contents
def makehtml():
    directoryhtml="<!DOCTYPE html> <html> <head> <title>Page Title</title> </head> <body> <h1>My First Heading</h1> <p>My first paragraph. </p> </body>\n</html\>"
    return directoryhtml
def SendFile(filepath):
    filepath2="./www"+filepath
    file = open(filepath2,'r')
    if file.name[len(file.name)-1] == "s":
        http_response = """HTTP/1.1 200 OK"""+"""<style Content-Type="text/css)"""+"""\r\n"""+ file.read() +"""</style>"""
    if file.name[len(file.name)-1] == "l":
        http_response = """HTTP/1.1 200 OK"""+"""Content-Type: text/html"""+"""\r\n""" +file.read() +""""""
    #else: 
     #   http_response = """HTTP/1.1 404"""
       
    return(http_response)
        


class MyWebServer(socketserver.BaseRequestHandler):
    
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print ("Got a request of: %s\n" % self.data)
        splitdata=str(self.data).split()
        print(splitdata[1])
    
        #headers = mimetools.Message(StringIO.StringIO
        
        if splitdata[1] == "/do-not-implement-this-page-it-is-not-found":

            self.request.sendall(bytearray(("""HTTP/1.1 404"""),'utf-8'))        
        if splitdata[1] == "/":
            response="""HTTP/1.1 200 OK """
            self.request.sendall(bytearray((response),'utf-8'))
            
        elif splitdata[1] == "/index.html" or "/base.css" or "/deep/index.html":
   
            self.request.sendall(bytearray(SendFile(splitdata[1]),'utf-8'))
            
       
        

if __name__ == "__main__":
    HOST, PORT = "localhost", 8080

    socketserver.TCPServer.allow_reuse_address = True
    # Create the server, binding to localhost on port 8080
    server = socketserver.TCPServer((HOST, PORT), MyWebServer)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
