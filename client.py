import socket
while True:
    ip = input()
    port = int(input())
    if ip == "close":
        break
    else:
        s = socket.socket()
        s.settimeout(1.5)
        if not s.connect_ex((ip, port)):
            print("Connect true")
            s.sendall("Connection".encode("utf-8"))
            data = s.recv(4096)
            print(f"Answer: {data.decode("utf-8")}")
        else:
            print("Connect false")
        s.close()
