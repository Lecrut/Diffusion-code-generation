import math

def area_of_ellipse(major_axis, minor_axis):
    semi_major = major_axis / 2.0
    semi_minor = minor_axis / 2.0
    return math.pi * semi_major * semi_minor

if __name__ == '__main__':
    major = 10.0
    minor = 6.0
    result = area_of_ellipse(major, minor)
    print(result)