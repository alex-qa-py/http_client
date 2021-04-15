import socket

HOST = "192.168.3.5"
PORT = 8888

my_socket = socket.socket()

address_and_port = ((HOST, PORT))
my_socket.bind(address_and_port)
print("Started socket on", address_and_port)

my_socket.listen()

conn, addr = my_socket.accept()
print("Got connection", conn, addr)

data = conn.recv(1024)
print("Got data", data)

conn.send(f"HTTP/1.1 200 OK\r\n Content-Length: 100\r\n Connection: close\r\n Content-Type: text/html\r\n\n <h1>{data.decode()}</h1>".encode("utf-8"))

my_socket.close()