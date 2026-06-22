import math

def calculate_ellipse_area(major_axis, minor_axis):
    return math.pi * major_axis * minor_axis

if __name__ == '__main__':
    major = 10.0
    minor = 5.0
    area = calculate_ellipse_area(major, minor)
    print(area)