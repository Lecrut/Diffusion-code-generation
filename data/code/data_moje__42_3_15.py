import math

def calculate_ellipse_area(major_axis, minor_axis):
    if major_axis <= 0 or minor_axis <= 0:
        raise ValueError('Major and minor axes must be positive numbers')
    semi_major = major_axis / 2
    semi_minor = minor_axis / 2
    return math.pi * semi_major * semi_minor
if __name__ == '__main__':
    major = 10
    minor = 5
    area = calculate_ellipse_area(major, minor)
    print(area)