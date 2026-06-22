import math

def ellipse_area(a, b):
    return math.pi * a * b

def rectangle_area(w, h):
    return w * h

def check_areas_equality():
    semi_major_axis = 5
    semi_minor_axis = 3
    width = 10
    height = 6
    
    area_ellipse = ellipse_area(semi_major_axis, semi_minor_axis)
    area_rectangle = rectangle_area(width, height)
    
    return area_ellipse == area_rectangle

if __name__ == '__main__':
    print(check_areas_equality())