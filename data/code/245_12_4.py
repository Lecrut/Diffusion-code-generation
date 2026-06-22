import math

def area_ellipse(semi_major_axis, semi_minor_axis):
    return math.pi * semi_major_axis * semi_minor_axis

def area_rectangle(width, height):
    return width * height

def check_area_equality(semi_major_axis=5, semi_minor_axis=3, width=10, height=6):
    ellipse_area = area_ellipse(semi_major_axis, semi_minor_axis)
    rectangle_area = area_rectangle(width, height)
    return ellipse_area == rectangle_area

if __name__ == '__main__':
    print(check_area_equality())