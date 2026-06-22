import math

def calculate_ellipse_area(semi_major_axis: float, semi_minor_axis: float) -> float:
    if semi_major_axis < 0 or semi_minor_axis < 0:
        raise ValueError("Semi-axes must be non-negative.")
    if semi_major_axis == 0 or semi_minor_axis == 0:
        return 0.0
    return math.pi * semi_major_axis * semi_minor_axis

if __name__ == '__main__':
    a = 5.0
    b = 3.0
    result = calculate_ellipse_area(a, b)
    print(result)