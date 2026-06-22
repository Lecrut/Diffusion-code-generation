import math

def calculate_ellipse_area(semi_major_axis, semi_minor_axis):
    if not isinstance(semi_major_axis, (int, float)) or not isinstance(semi_minor_axis, (int, float)):
        raise TypeError("Inputs must be numbers")
    if semi_major_axis <= 0 or semi_minor_axis <= 0:
        raise ValueError("Inputs must be positive numbers")
    area = math.pi * semi_major_axis * semi_minor_axis
    return area

if __name__ == '__main__':
    print(calculate_ellipse_area(5, 3))
    print(calculate_ellipse_area(10, 10))
    print(calculate_ellipse_area(7.5, 2.5))