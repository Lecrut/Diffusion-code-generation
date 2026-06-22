import math

def area_circle(radius):
    return math.pi * radius ** 2

def area_rectangle(length, width):
    return length * width

if __name__ == '__main__':
    circle_radius = 5
    rectangle_length = 10
    rectangle_width = 7
    
    circle_area = area_circle(circle_radius)
    rectangle_area = area_rectangle(rectangle_length, rectangle_width)
    
    total_area = circle_area + rectangle_area
    print(total_area)