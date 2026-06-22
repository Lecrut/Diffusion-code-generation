import math

def ellipse_area(major_axis, minor_axis):
    semi_major = major_axis / 2.0
    semi_minor = minor_axis / 2.0
    area = math.pi * semi_major * semi_minor
    return area

if __name__ == '__main__':
    major = 10.0
    minor = 6.0
    result = ellipse_area(major, minor)
    print(result)