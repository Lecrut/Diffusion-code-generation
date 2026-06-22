import math

def ellipse_area(major_axis, minor_axis):
    return math.pi * (major_axis / 2) * (minor_axis / 2)

if __name__ == '__main__':
    major = 10.0
    minor = 5.0
    print(ellipse_area(major, minor))