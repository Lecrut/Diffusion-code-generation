import math

def calculate_ellipse_area(semi_major_axis, semi_minor_axis):
    return math.pi * semi_major_axis * semi_minor_axis

if __name__ == '__main__':
    semi_major = 5.0
    semi_minor = 3.0
    area = calculate_ellipse_area(semi_major, semi_minor)
    print(area)