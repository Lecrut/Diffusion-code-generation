import math

def ellipse_area(a: float, b: float) -> float:
    return math.pi * a * b

if __name__ == '__main__':
    major_axis = 5.0
    minor_axis = 3.0
    area = ellipse_area(major_axis, minor_axis)
    print(area)