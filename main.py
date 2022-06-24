import pygame, math, sys

win=pygame.display.set_mode((400,400))
pygame.display.set_caption("Level set")
clock=pygame.time.Clock()
fps=60


def function(x,y):
    try:
        output = x*y
    except:
        output = "nan"
    return output

def draw(i,j,output,d,min_):
    if(d != 0):
        q=(output-min_)/d
    else:
        q=1/2
    
    R=max(0,-2*abs(q-1)+1)
    G=max(0,-2*(abs(q-1/2))+1)
    B=max(0,-2*abs(q*q)+1)

    h=20
    R=math.floor(R*h)/h
    G=math.floor(G*h)/h
    B=math.floor(B*h)/h

    R=R*255
    G=G*255
    B=B*255

    pygame.draw.rect(win,(R,G,B),(i,400-j-1,1,1))
    

def main():
    interval_x=(-1,1)
    interval_y=(-1,1)
    
    max_,min_=function(interval_x[0],interval_y[0]),function(interval_x[0],interval_y[0])
    L=[]
    
    for i in range(0,400,1):
        for j in range(0,400,1):
            x=interval_x[0]+((i*(interval_x[1]-interval_x[0]))/400)
            y=interval_y[0]+((j*(interval_y[1]-interval_y[0]))/400)
            output=function(x,y)
            if(output != "nan"):
                if(max_<output):
                    max_=output
                if(min_>output):
                    min_=output
                min_=max(-10,min_)
                max_=min(10,max_)
            
            L.append((i,j,output))
            
    d=max_-min_
    for i in range(0,len(L),1):
        if(L[i][2] != "nan"):
            draw(L[i][0],L[i][1],L[i][2],d,min_)
            
    return
if __name__ == "__main__":
    main()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
    clock.tick(fps)