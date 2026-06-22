import math

def calculate_ellipse_area(semi_major_axis, semi_minor_axis):
    if semi_major_axis <= 0 or semi_minor_axis <= 0:
        raise ValueError("Semi-axes must be positive numbers")
    return math.pi * semi_major_axis * semi_minor_axis

if __name__ == '__main__':
    semi_major = 5
    semi_minor = 3
    area = calculate_ellipse_area(semi_major, semi_minor)
    print(area)