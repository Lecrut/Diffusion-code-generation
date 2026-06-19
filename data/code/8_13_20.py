import math

def scaled_area_rectangle(length, width, scale_factor):
    return (length * width) * scale_factor

def scaled_area_circle(radius, scale_factor):
    return (math.pi * radius ** 2) * scale_factor

if __name__ == '__main__':
    length = 5.0
    width = 3.0
    rectangle_scale_factor = 2.0
    radius = 4.0
    circle_scale_factor = 1.5
    
    rectangle_area = scaled_area_rectangle(length, width, rectangle_scale_factor)
    circle_area = scaled_area_circle(radius, circle_scale_factor)
    
    print(rectangle_area)
    print(circle_area)