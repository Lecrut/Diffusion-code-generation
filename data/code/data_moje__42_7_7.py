import math

def calculate_ellipse_area(semi_major_axis: float, semi_minor_axis: float) -> float:
    if semi_major_axis <= 0:
        raise ValueError("Semi-major axis must be positive.")
    if semi_minor_axis <= 0:
        raise ValueError("Semi-minor axis must be positive.")
    return math.pi * semi_major_axis * semi_minor_axis

if __name__ == '__main__':
    result = calculate_ellipse_area(5.0, 3.0)
    print(result)