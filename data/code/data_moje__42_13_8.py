import math

def ellipse_area(a, b):
    return math.pi * a * b

if __name__ == '__main__':
    semi_major_axis = 5.0
    semi_minor_axis = 3.0
    area = ellipse_area(semi_major_axis, semi_minor_axis)
    print(area)