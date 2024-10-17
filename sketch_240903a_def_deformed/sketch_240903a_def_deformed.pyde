import math

w, h = 1080, 1920
colors = [(219, 177, 188), (211, 196, 227), (143, 149, 211), (137, 218, 255)]
current_size = 3848
size_decrement = 7  # The amount to decrease the size each frame
min_size = 0        # Minimum size to stop the loop

# Variables for bouncing camera effect
camera_y = h / 2  # Start camera in the middle of the screen
bounce_speed = random(0,0.3)  # Adjust for faster or slower bouncing
bounce_height = random(30)  # Max height for the bounce
frame_count = 0     # Keeps track of frames

def get_color(l):
    return l[int(random(len(l)))]

def deformed_circle(x, y, r):
    pushMatrix()
    translate(x, y)
    
    points = []
    for i in range(0, 360, 15):
        points.append((r / 2 * sin(radians(i)), r / 2 * cos(radians(i))))
    
    # Create deformed circles
    final = []
    for p in points:
        x_change = p[0] / 55.0
        y_change = p[1] / 55.0  
        change = random(-3, 3)
        p = (p[0] + x_change * change, p[1] + y_change * change)
        final.append(p)
        
    # Create outline and deformed shape
    fill(*get_color(colors))
    strokeWeight(5)    
    beginShape()
    for p in final:
        curveVertex(*p)
    curveVertex(*final[0])
    curveVertex(*final[1])
    curveVertex(*final[2])
    curveVertex(*final[3])
    endShape()
    popMatrix()

def setup():
    size(w, h)
    pixelDensity(2)
    frameRate(30)  

def draw():
    global current_size, camera_y, frame_count
    
    background(255)
    strokeWeight(1)
    noFill()
    
    # Update the camera's y-position to simulate bouncing
    camera_y = h / 2 + math.sin(frame_count * bounce_speed) * bounce_height
    frame_count += 1 
    
    # Draw multiple circles, getting smaller each time
    temp_size = current_size
    while temp_size > min_size:
        deformed_circle(w/2, camera_y, temp_size)  
        temp_size -= size_decrement 
    
    # Decrease the starting size for the next frame
    if current_size > min_size:
        current_size -= size_decrement
    else:
        noLoop()  

    # Save frames for creating the animation
    saveFrame("D:/Processing/processing-3.5.4/frames/frame_####.png")
