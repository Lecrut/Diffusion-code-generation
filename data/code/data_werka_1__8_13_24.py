import math

def scaled_area_rectangle(length, width, scale):
    return length * width * scale

def scaled_area_circle(radius, scale):
    return math.pi * radius ** 2 * scale

if __name__ == '__main__':
    rect_length = 5.0
    rect_width = 3.0
    rect_scale = 2.0
    circle_radius = 4.0
    circle_scale = 1.5
    
    print(scaled_area_rectangle(rect_length, rect_width, rect_scale))
    print(scaled_area_circle(circle_radius, circle_scale))