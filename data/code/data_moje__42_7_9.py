import math

def calculate_ellipse_area(a: float, b: float) -> float:
    if a <= 0:
        raise ValueError("Semi-major axis must be positive.")
    if b <= 0:
        raise ValueError("Semi-minor axis must be positive.")
    return math.pi * a * b

if __name__ == '__main__':
    a_value = 5.0
    b_value = 3.0
    result = calculate_ellipse_area(a_value, b_value)
    print(result)