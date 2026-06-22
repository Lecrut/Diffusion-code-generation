import math

def ellipse_area(semi_major_axis, semi_minor_axis):
    if semi_major_axis <= 0 or semi_minor_axis <= 0:
        raise ValueError("Axes must be positive numbers")
    return math.pi * semi_major_axis * semi_minor_axis

if __name__ == '__main__':
    print(ellipse_area(5, 3))
    print(ellipse_area(10, 7))
    print(ellipse_area(1, 1))