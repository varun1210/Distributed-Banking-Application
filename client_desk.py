import socket;
import threading;
import time

acc_no=[]  #integer

time_stamp=[] #integer




def request():
    try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
            print("Requesting Initiated........");
            
    except socket.error as err:
            print("Could not setup socket");	
    port = 12365;
    ip ='192.168.43.179' 

    with s:
            s.connect((ip,port));

            rec = s.recv(1024);#1
            print(rec.decode());

            choice = input()
            data_sent = choice.encode();#2ENTER CHOICE
            s.sendall(data_sent);
            choice=int(choice)

            rec = s.recv(1024);#3
            print(rec.decode());
            
            req_account = (input()).encode();#4 ENTER ACCOUNT NO
            s.sendall(req_account);
            acc_no.append(int(req_account))


            if choice==1:
                rec = s.recv(1024);#1.1
                print(rec.decode());
                Name=input()
                data_sent = Name.encode();#1.2
                s.sendall(data_sent);

                rec = s.recv(1024);#1.3
                print(rec.decode());
                balance=input()
                data_sent = balance.encode();#1.4
                s.sendall(data_sent);

                rec = s.recv(1024);#1.5
                print(rec.decode())
                
            elif choice==4:
                rec = s.recv(1024);#1.3
                print(rec.decode())
            elif choice==2 or choice==3 or choice==5:

                allocated_time_stamp=s.recv(1024)  #storing allocated timestamp
                allocated_time_stamp=float(allocated_time_stamp.decode())
                time_stamp.append(allocated_time_stamp)

                rec=s.recv(1024)  ##printing wait message
                print(rec.decode())

                
                acc_no.append(req_account)    #
                
    #print("Connection closed\n\n");
    s.close();
    #serving(int(choice))




def broad_cast_sender_receiver():
        try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
                print("Ready For Broadcast initiated");

        except socket.error as err:
                print("Socket creation failed");
                
        port = 12399;
        s.bind(('', port));
        print("Socket binded to: ", port);
        s.listen(5);
        print("Socket is listening");
        while True:
                conn, add = s.accept();
                with conn:
                        print("Got connection from ",add);
                        conn.send(b"Connection successful");
                        
                        acc = conn.recv(1024);
                        acc=acc.decode()
                        acc=int(acc)

                        tim=conn.recv(1024)
                        tim=tim.decode()
                        tim=int(tim)

                        print(str(acc))
                        print(str(tim))

                        if acc==-1:
                                data_sent = ("Thank You").encode()
                                print(data_sent)
                                conn.sendall(data_sent);
                                execute()
                                s.close();
                                print("Permission Granted")
                                return;
                        elif acc_no[0]==acc and time_stamp[0]<=tim:
                                data_sent = (str(0)).encode()
                                print("cond 2")
                                conn.sendall(data_sent);
                        else:
                                data_sent = (str(1)).encode()
                                conn.sendall(data_sent);
                                
        s.close();
                                
                        
    
def execute():
        try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
                print("Waiting For Response................");

        except socket.error as err:
                print("Socket creation failed");
                
        port = 12000;
        s.bind(('', port));
        print("Socket binded to: ", port);
        s.listen(5);
        print("Socket is listening");

        while True:
                conn, add = s.accept();
                with conn:
                        print("Got connection from ",add);
                        conn.send(b"Connection successful");

                        data = conn.recv(1024);
                        t=data.decode()
                        #choice=int(t)

                        if t=="3" or t=="2":
                            data = conn.recv(1024);
                            print(data.decode())

                            amount=input()
                            data_sent=amount.encode()
                            conn.sendall(data_sent)

                            data = conn.recv(1024);
                            print(data.decode())
                        else:
                            data = conn.recv(1024);
                            print(data.decode())

                            acc_no=input()
                            data_sent=acc_no.encode()
                            conn.sendall(data_sent)

                            
                            data = conn.recv(1024);
                            print(data.decode())

                            amount=input()
                            data_sent=amount.encode()
                            conn.sendall(data_sent)

                            data = conn.recv(1024);
                            print(data.decode())
        s.close();



def requesting():
    request()
def executing():
    execute()
def broadcasting():
    broad_cast_sender_receiver()
    


if __name__ == '__main__':
    requesting()
    broadcasting()
    











































    
        
