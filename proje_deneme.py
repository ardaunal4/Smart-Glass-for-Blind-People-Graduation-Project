import cv2
import numpy as np
import math
import vlc
import time
import os

#def distance():
b = 7                                                                                                             # cm
angle = 85                                                                                                        # degree
t = 320                                                                                                           # pixel
pi = 3.1415926

folder = "/home/pi/Desktop/blindpeople/sesler/"
file_list = os.listdir(folder)
def ses(name, distance):                                                                                          # voice function                                                                    
    dist = round(0.01*distance)
    for file_name in file_list:
        if file_name == name + ".mpeg":
            player = vlc.MediaPlayer(folder + name + ".mpeg")
            player.play()
            playerdist = vlc.MediaPlayer(folder + str(dist) + ".mpeg")
            playerdist.play()

kamera = cv2.VideoCapture(0)
mesafe_yuz = 500
mesafe_sira = 500
mesafe_car = 500

while True:                                                                                                       # program starts                                                                                                  
    ret,kare = kamera.read()
    gri_kare = cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)

    yuz_casc = cv2.CascadeClassifier("yuz.xml")
    car_casc = cv2.CascadeClassifier("cars.xml")
    desk_casc = cv2.CascadeClassifier("desk.xml")

    yuzler = yuz_casc.detectMultiScale(gri_kare,1.1,5)
    car = car_casc.detectMultiScale(gri_kare,1.1,5)
    sira = desk_casc.detectMultiScale(gri_kare,1.1,5)

    print(yuzler, car, sira)

    
    #cv2.imshow("Yuz Tanıma",gri_kare)

                                                                                                                   # Face recognition script with distance measurement method
    if len(yuzler) < 3 and len(yuzler) > 1:
        first_array = yuzler[0]
        second_array = yuzler[1]
        if first_array[0] < 320:
            xbir = first_array[0] + first_array[2]/2 - t/2
            xiki = second_array[0] + second_array[2]/2 - t/2 - 320
        else:
            xbir = first_array[0] + first_array[2]/2 - t/2 - 320
            xiki = second_array[0] + second_array[2] / 2 - t / 2
        distance = abs( (b * t) / (2 * math.tan(pi * angle / 360) * (xbir - xiki)))
        mesafe_yuz = distance
        print(mesafe_yuz)

    elif len(yuzler)>3:
        k=0
        j=0
        x1=0
        x2 = 0
        for k in range(len(yuzler)):
            for j in range(len(yuzler)):
                if abs(yuzler[k][0]-yuzler[j][0])<300 and abs(yuzler[k][0]-yuzler[j][0])>280:
                    x1 = yuzler[k][0]
                    if x1 != x2:
                        print("x1 = ", yuzler[k][0])
                        print("x2 = ", yuzler[j][0])
                        x2 = yuzler[j][0]
                        if x1 < 320:
                            xbir = x1 + yuzler[k][2]/2 - t/2
                            xiki = x2 + yuzler[j][2]/2 - t/2 - 320
                        elif x1 > 319:
                            xbir = x1 + yuzler[k][2]/2 - t/2 - 320
                            xiki = x2 + yuzler[j][2] / 2 - t / 2
                        distance = abs( (b * t) / (2 * math.tan(pi * angle / 360) * (xbir - xiki)))
                        if mesafe_yuz > distance:
                            mesafe_yuz = distance
                            print(mesafe_yuz)
                                                                                                                      # Car recognition script with distance measurement method
    if len(car) < 3 and len(car) > 1:
        first_array = car[0]
        second_array = car[1]
        if first_array[0] < 320:
            xbir = first_array[0] + first_array[2]/2 - t/2
            xiki = second_array[0] + second_array[2]/2 - t/2 - 320
        else:
            xbir = first_array[0] + first_array[2]/2 - t/2 - 320
            xiki = second_array[0] + second_array[2] / 2 - t / 2
        distance = abs( (b * t) / (2 * math.tan(pi * angle / 360) * (xbir - xiki)))
        mesafe_car = distance
    elif len(car)>2:
        k=0
        j=0
        x1 = 0
        x2 = 0
        for k in range(len(car)):
            for j in range(len(car)):
                if abs(car[k][0]-car[j][0])<300 and abs(car[k][0]-car[j][0])>280:
                    x1 = car[k][0]
                    if x1 != x2:
                        print("x1 = ", car[k][0])
                        print("x2 = ", car[j][0])
                        x2 = car[j][0]
                        if x1 < 320:
                            xbir = x1 + car[k][2]/2 - t/2
                            xiki = x2 + car[j][2]/2 - t/2 - 320
                        elif x1 >319:
                            xbir = x1 + car[k][2]/2 - t/2 - 320
                            xiki = x2 + car[j][2] / 2 - t / 2
                        distance = abs( (b * t) / (2 * math.tan(pi * angle / 360) * (xbir - xiki)))
                        if mesafe_car > distance:
                            mesafe_car = distance

                                                                                                                         # Desk recogition script with distance measurement method
    if len(sira) < 3 and len(sira) > 1:
        first_array = sira[0]
        second_array = sira[1]
        if first_array[0] < 320:
            xbir = first_array[0] + first_array[2] / 2 - t / 2
            xiki = second_array[0] + second_array[2] / 2 - t / 2 - 320
        else:
            xbir = first_array[0] + first_array[2] / 2 - t / 2 - 320
            xiki = second_array[0] + second_array[2] / 2 - t / 2
        distance = abs((b * t) / (2 * math.tan(pi * angle / 360) * (xbir - xiki)))
        mesafe_sira = distance
    elif len(sira) > 2:
        k = 0
        j = 0
        x1 = 0
        x2 = 0
        for k in range(len(sira)):
            for j in range(len(sira)):
                if abs(sira[k][0] - sira[j][0]) < 300 and abs(sira[k][0] - sira[j][0]) > 280:
                    x1 = sira[k][0]
                    if x1 != x2:
                        print("x1 = ", sira[k][0])
                        print("x2 = ", sira[j][0])
                        x2 = sira[j][0]
                        if x1 < 320:
                            xbir = x1 + sira[k][2] / 2 - t / 2
                            xiki = x2 + sira[j][2] / 2 - t / 2 - 320
                        elif x1 > 319:
                            xbir = x1 + sira[k][2] / 2 - t / 2 - 320
                            xiki = x2 + sira[j][2] / 2 - t / 2
                        distance = abs((b * t) / (2 * math.tan(pi * angle / 360) * (xbir - xiki)))
                        if mesafe_sira > distance:
                            mesafe_sira = distance

        # Closest distance
    if mesafe_yuz < mesafe_sira and mesafe_yuz < mesafe_car:
        ses("yuz", mesafe_yuz)
        print(ses)
    elif mesafe_sira < mesafe_yuz and mesafe_sira < mesafe_car:
        ses("masa", mesafe_sira)
    elif mesafe_car < mesafe_sira and mesafe_car < mesafe_yuz:
        ses("araba", mesafe_car)

    if cv2.waitKey(1000) & 0xFF == ord("q"):
        break

kamera.release()
cv2.destroyAllWindows()
