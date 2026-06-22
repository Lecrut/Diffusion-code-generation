import math

def calculate_ellipse_area(major_axis, minor_axis):
    semi_major = major_axis / 2
    semi_minor = minor_axis / 2
    return math.pi * semi_major * semi_minor

if __name__ == '__main__':
    major_axis_value = 10
    minor_axis_value = 6
    area = calculate_ellipse_area(major_axis_value, minor_axis_value)
    print(area)