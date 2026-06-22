import math

def ellipse_area(major_axis, minor_axis):
    a = major_axis / 2
    b = minor_axis / 2
    return math.pi * a * b

if __name__ == '__main__':
    major = 10
    minor = 5
    area = ellipse_area(major, minor)
    print(area)