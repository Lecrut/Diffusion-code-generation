import math

def calculate_ellipse_area(major_axis, minor_axis):
    a = major_axis / 2
    b = minor_axis / 2
    return math.pi * a * b

if __name__ == '__main__':
    area = calculate_ellipse_area(10, 6)
    print(area)