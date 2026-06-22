import math

def ellipse_area(major_axis, minor_axis):
    semi_major = major_axis / 2
    semi_minor = minor_axis / 2
    return math.pi * semi_major * semi_minor

if __name__ == '__main__':
    major = 10
    minor = 6
    area = ellipse_area(major, minor)
    print(area)