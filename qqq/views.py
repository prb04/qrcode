from django.shortcuts import render
from django.http import HttpResponse
import qrcode
import cv2
import pyzbar.pyzbar as pyzbar




def index(request):
    
    return render(request,"home.html",{'name':'Pranay'})

def generate(request):
            
    input_data = request.GET['data']
    #Creating an instance of qrcode
    qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5)
    qr.add_data(input_data)
    qr.make(fit=True)
    img = qr.make_image(back_color = "white", fill_color="red")
    img.save('C:/Users/prana/Desktop/pirooo/qrc/static/images/qrcode001.png')

    return render(request,"result.html",{'result':img})


def scan(request):
    cap = cv2.VideoCapture(0)
    while 1:
        _, frame = cap.read()
        decodedObject = pyzbar.decode(frame)
        Data = ''
        for obj in decodedObject:
            Data = obj.data.decode("UTF-8")
            print("Type:", obj.type)
            print("Data:", obj.data)

        cv2.imshow("Frame", frame)


        key = cv2.waitKey(1)
        if Data != '':
            break
        
    return render(request,"res.html",{'result':Data})

