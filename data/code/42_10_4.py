import math

def calculate_ellipse_area(major_axis, minor_axis):
    return math.pi * (major_axis / 2) * (minor_axis / 2)

if __name__ == '__main__':
    major = 10
    minor = 5
    area = calculate_ellipse_area(major, minor)
    print(area)