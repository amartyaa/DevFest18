import pyrebase
import bluetooth 
config = {
  "apiKey": "Hidden",
  "authDomain": "Hidden",
  "databaseURL": "Hidden",
  "storageBucket": "Hidden"
}
######INITIALISE FIREBASE
firebase = pyrebase.initialize_app(config)
db= firebase.database()
##########Initialize bluetooth
server_socket=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
port = 1
server_socket.bind(("",port))
server_socket.listen(1)
client_socket,address = server_socket.accept()
print ("Accepted connection from ",address)

while 1:
 
 d = client_socket.recv(1024)
 c=str(d)
 data=c[2]
 print("Received: %s" % data)
 data = {"name": data}
 db.child("users").child("Data2").set(c)
 db.child("users").child("Data2").set(data)
 '''if (data == "0"):    #if '0' is sent from the Android App, turn OFF the LED
  print ("GPIO 21 LOW, LED OFF")
  #GPIO.output(LED,0)
 if (data == "1"):    #if '1' is sent from the Android App, turn OFF the LED
  print ("GPIO 21 HIGH, LED ON")
  #GPIO.output(LED,1)'''
 if (data == "q"):
  print ("Quit")
  break
 
client_socket.close()
server_socket.close()
