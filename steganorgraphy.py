"""
Steganogaphy Code
"""
from PIL import Image

def genData(data):
    newd = []
    
    for i in data:
        newd.append(format(ord(i), '08b'))
    return newd

def modPix(pix, data):
    
    datalist = genData(data)
    lendata = len(datalist)
    imdata = iter(pix)
    
    for i in range(lendata):
        pix = [value for value in imdata.__next__()[:3] +
                                imdata.__next__()[:3] +
                                imdata.__next__()[:3]]
        
        for j in range(0, 8):
            if (datalist[i][j] == '0' and pix[j]% 2 !=0):
                pix[j] -= 1
                
            elif (datalist[i][j] == '1' and pix[j] % 2 == 0):
                if(pix[j] != 0):
                    pix[j] -= 1
                else:
                    pix[j] += 1
        
        if (i == lendata - 1):
            if(pix[-1] % 2 == 0):
                if(pix[-1] != 0):
                    pix[-1] -= 1
                else:
                    pix[-1] += 1
        
        else:
            if (pix[-1] % 2 != 0):
                pix[-1] -= 1
        
        
