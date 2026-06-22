import math

def ellipse_area(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Axis lengths must be positive")
    return math.pi * a * b

if __name__ == '__main__':
    major_axis = 5.0
    minor_axis = 3.0
    area = ellipse_area(major_axis, minor_axis)
    print(area)