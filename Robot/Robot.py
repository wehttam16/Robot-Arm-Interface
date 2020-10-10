import serial
import time
import tkinter 

#PORT DECLARATIONS
port = 'COM4' #SEE PORT NAME IN ARDUINO IDE: TOOLS>PORT:
baud = 115200 #BY DEFAULT 115200
timeout = None #LEAVE AS IS
ser = serial.Serial(port,baud,timeout=timeout)
time.sleep(2)

root = tkinter.Tk()
root.minsize(300, 50)
root.title("Robot Helper")
root.iconbitmap('Robots.jpg')


#LIST OF COMMANDS TO BE EXECUTED BY ROBOT ARM, CHANGE ACCORDINGLY
cmdList = [
"G0 X180 Y0 Z120 F165 ",
"G0 X180 Y0 Z-120 F165",
"G0 X180 Y0 Z120 F165",
"G0 X0 Y170 Z120 F165",
"G0 X-180 Y0 Z120 F165",
"G0 X-180 Y0 Z-120 F165",
"G0 X-180 Y0 Z120 F165",
"G0 X0 Y170 Z120 F165",

]

bCmdList = []
for cmd in cmdList:
    cmd_temp = cmd + '\r'
    bCmdList.append(cmd_temp.encode('utf-8'))



def wait_complete():
    waitstatus = 1
    while True:
        a = ser.readline()
        if "ok" in a.decode("utf-8"):
            waitstatus = 0
            break

def Homing():
    ser.write(b'G28\r')
    print("homing in progress")
    time.sleep(10)
    
def Printing():
    for bCmd in bCmdList:
        ser.write(bCmd)
        print(bCmd)
        wait_complete()
    
frame = tkinter.Frame(root)
frame.pack()

button = tkinter.Button(frame, text="QUIT",fg="red",command=quit)
button.pack(side=tkinter.LEFT)

Home = tkinter.Button(frame,text="HOME",command=Homing)
Home.pack(side=tkinter.LEFT)

Print = tkinter.Button(frame,text="MOVE",command=Printing)
Print.pack(side=tkinter.LEFT)

#ROBOT HOMES ITSELF
ser.write(b'G28\r')
print("Homing in progress")
time.sleep(10)
print(ser.readline())

root.mainloop()




        
    
    
