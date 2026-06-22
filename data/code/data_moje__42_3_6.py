import math

def area_of_ellipse(major_axis, minor_axis):
    semi_major = major_axis / 2
    semi_minor = minor_axis / 2
    return math.pi * semi_major * semi_minor

if __name__ == '__main__':
    result = area_of_ellipse(10, 6)
    print(result)