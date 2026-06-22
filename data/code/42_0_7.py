import math

def calculate_ellipse_area(major_axis, minor_axis):
    a = major_axis / 2.0
    b = minor_axis / 2.0
    return math.pi * a * b

if __name__ == '__main__':
    major = 10.0
    minor = 6.0
    area = calculate_ellipse_area(major, minor)
    print(area)