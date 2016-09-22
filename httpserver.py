#!/usr/bin/python
#
######
#
# Simplest python http server serving inline string v0.1
#
#####

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',80))

while 1:
  s.listen(5)
  conn,addr = s.accept()
  # print "Connected by ", addr

  databuf=""

  while 1:
    data = conn.recv(433)
    databuf += data
    if databuf[-4:] == '\r\n\r\n' : break

  # print "data length was: ", len(databuf)
  conn.send('<h1>Hello World\n')
  conn.close()

