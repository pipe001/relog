Ya = 0
Yb = 0
Yc = 0

def setup():

    size(300, 300)

    
def draw():

    background(0)
    
    global Ya
    global Yb
    global Yc
    

    circle (50, Ya, 40)

    if Ya > height: 
       Ya = 0 
       
    else: 
     Ya = map(second(), 0, 59, 0, height)


    circle (150, Yb, 40)

    if Yb > height:
        Yb = 0
     
    else:  
     Yb = map(minute(), 0, 59, 0, height)
       
    circle (250, Yc, 40)

    if Yc > height:
       Yc = 0
     
    else:  
       Yc = map(hour(), 0, 23, 0, height)
