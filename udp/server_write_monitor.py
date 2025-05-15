import socket
import datetime

def start_server( host: str, port: int):
    server_read = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_read.bind((host, port))
    print(f"Server  [MONITOR] started at {host}:{port}\n Listening now...")

    while True:
        data, addr = server_read.recvfrom(1024)
        message = data.decode('utf-8').split(',')

        time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"[{time}][{message[0].upper()}]: {message[1]}")


if __name__=='__main__':

    HOST = 'localhost'
    PORT = 9000

    start_server(HOST, PORT)
