import math

def ellipse_area(major_axis: float, minor_axis: float) -> float:
    a = major_axis / 2.0
    b = minor_axis / 2.0
    return math.pi * a * b

if __name__ == '__main__':
    major = 10.0
    minor = 6.0
    result = ellipse_area(major, minor)
    print(result)