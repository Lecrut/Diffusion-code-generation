import math

def calculate_ellipse_area(major_axis, minor_axis):
    return math.pi * major_axis * minor_axis

if __name__ == '__main__':
    result = calculate_ellipse_area(5, 3)
    print(result)