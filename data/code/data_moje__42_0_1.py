import math

def calculate_ellipse_area(major_axis, minor_axis):
    a = major_axis / 2.0
    b = minor_axis / 2.0
    area = math.pi * a * b
    return area

if __name__ == '__main__':
    major = 10
    minor = 6
    result = calculate_ellipse_area(major, minor)
    print(result)