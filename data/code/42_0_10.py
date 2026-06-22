import math

def calculate_ellipse_area(major_axis_length, minor_axis_length):
    semi_major = major_axis_length / 2.0
    semi_minor = minor_axis_length / 2.0
    area = math.pi * semi_major * semi_minor
    return area

if __name__ == '__main__':
    major = 14.0
    minor = 8.0
    result = calculate_ellipse_area(major, minor)
    print(result)