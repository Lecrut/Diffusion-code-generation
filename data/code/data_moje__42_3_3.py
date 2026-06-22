import math

def calculate_ellipse_area(major_axis: float, minor_axis: float) -> float:
    if major_axis <= 0 or minor_axis <= 0:
        raise ValueError("Major and minor axes must be positive numbers")
    return math.pi * major_axis * minor_axis

if __name__ == '__main__':
    major = 5.0
    minor = 3.0
    area = calculate_ellipse_area(major, minor)
    print(area)