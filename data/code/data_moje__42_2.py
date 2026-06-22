import math

def calculate_ellipse_area(semi_major, semi_minor):
    return math.pi * semi_major * semi_minor

if __name__ == '__main__':
    semi_major_axis = 5.0
    semi_minor_axis = 3.0
    area = calculate_ellipse_area(semi_major_axis, semi_minor_axis)
    print(area)