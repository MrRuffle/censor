

# Hover mouse over image to censor it

#flag.png 300, 200
#flower.jpg 533, 800
 # 10*10 kockák
 # 100*100


w = 533
h = 800
cens = 20 # size of small squares
squares = 10 # number of small squares in a row

def setup():

    size(w,h)    
    global img
    img = loadImage("flower.jpg")
    image(img,0,0)
    
def draw():
    
    # x + y*width
    r = 0
    g = 0
    b = 0
    cols = 0
   
    image(img,0,0)
    loadPixels()
  
    noCursor()
    noStroke()
    for m in range(squares):
        for n in range(squares):
            for i in range(cens):
                for j in range(cens):
                    if mouseY < h-(cens*n+i) and mouseX < w-(cens*m+j):
                        cols = (mouseX+j+(cens*m)) + (mouseY+i+(cens*n))*w
                        r += red(pixels[cols])
                        b += blue(pixels[cols])
                        g += green(pixels[cols])
            r /= cens*cens
            g /= cens*cens
            b /= cens*cens
            fill(r,g,b)
            rect(mouseX+cens*m, mouseY+cens*n, cens, cens)
