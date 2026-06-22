import math

def calculate_ellipse_area(major_axis, minor_axis):
    return math.pi * major_axis * minor_axis

if __name__ == '__main__':
    major_axis_length = 10
    minor_axis_length = 5
    area = calculate_ellipse_area(major_axis_length, minor_axis_length)
    print(area)