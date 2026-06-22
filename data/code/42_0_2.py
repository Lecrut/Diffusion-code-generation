import math

def calculate_ellipse_area(major_axis, minor_axis):
    a = major_axis / 2
    b = minor_axis / 2
    return math.pi * a * b

if __name__ == '__main__':
    major_axis_length = 10
    minor_axis_length = 6
    area = calculate_ellipse_area(major_axis_length, minor_axis_length)
    print(area)