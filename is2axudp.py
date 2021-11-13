#!/usr/bin/python3
import socket
from wx import sendax 

RECV_BUFFER_LENGTH=1500

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# bind the socket to a public host, and a well-known port
serversocket.bind(("0.0.0.0", 1234))
# become a server socket
serversocket.listen(5)

while True:
    # accept connections from outside
    (clientsocket, address) = serversocket.accept()
    print("connection")
    clientsocket.send(b"# is2axudp 0.1\n")
    print("<-# is2axudp 0.1")
    data = clientsocket.recv(RECV_BUFFER_LENGTH)
    print("->"+data.decode('cp1250'))
    clientsocket.send(b"# logresp #\n")
    print("<-# logresp #")
    data = clientsocket.recv(RECV_BUFFER_LENGTH)
    print("->"+data.decode('cp1250'))
    data = data.replace(b',TCPIP*',b',WIDE1-1')
    sendax(data,("127.0.0.1",9999),{})
    print("<~"+data.decode('cp1250'))

    clientsocket.close()