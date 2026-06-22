import math

def calculate_ellipse_area(major_axis, minor_axis):
    semi_major = major_axis / 2
    semi_minor = minor_axis / 2
    area = math.pi * semi_major * semi_minor
    return area

if __name__ == '__main__':
    major = 10
    minor = 6
    result = calculate_ellipse_area(major, minor)
    print(result)