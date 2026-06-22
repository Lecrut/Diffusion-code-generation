import math

def calculate_ellipse_area(major_axis, minor_axis):
    return math.pi * major_axis * minor_axis

if __name__ == '__main__':
    major_length = 10
    minor_length = 5
    area = calculate_ellipse_area(major_length, minor_length)
    print(area)