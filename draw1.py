from Focus_Roots import *

def change ():
    set_background(color_burlywood)
    draw_circle(190,140,50,0,color=color_chocolate) #ears
    draw_circle(190,140,50,6,color=color_brown) #ears
    draw_ellipse(80,310,140,90,0,color=color_chocolate) #arms
    draw_ellipse(80,310,140,90,6,color=color_brown) #arms
    draw_circle(250,250,120,0,color=color_chocolate) #head
    draw_circle(250,250,120,6,color=color_brown) #head
    draw_circle(300,140,50,0,color=color_chocolate) #ears
    draw_ellipse(250,200,30,80,0,color=color_black) #eyes
    draw_ellipse(170,200,30,80,0,color=color_black) #eyes
    draw_ellipse(250,230,30,50,0,color=color_mid_night_blue) #eyes
    draw_ellipse(170,230,30,50,0,color=color_mid_night_blue) #eyes
    draw_ellipse(180,200,10,20,0,color=color_white) #eyes
    draw_ellipse(260,200,10,20,0,color=color_white) #eyes
    draw_ellipse(140,280,235,245,0,color=color_chocolate) #body
    draw_ellipse(300,310,140,90,0,color=color_chocolate) #arms
    draw_ellipse(300,310,140,90,6,color=color_brown) #arms
    draw_circle(300,340,50,0,color=color_chocolate) #arms
    draw_line([230,300],[250,290],6,color=color_black)
    draw_line([210,290],[230,300],6,color=color_black)
    write_text("Happy Bear",250,50,40,color=color_orchid)
    
    






draw(change)