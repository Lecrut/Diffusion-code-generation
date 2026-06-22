import math

def trapezoid_area(base_a, base_b, height):
    if not isinstance(base_a, (int, float)) or not isinstance(base_b, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Arguments must be numeric.")
    if base_a <= 0 or base_b <= 0 or height <= 0:
        raise ValueError("Bases and height must be positive.")
    if math.isinf(base_a) or math.isinf(base_b) or math.isinf(height):
        raise ValueError("Arguments must be finite.")
    mid = (base_a + base_b) / 2.0
    return mid * height

if __name__ == '__main__':
    result = trapezoid_area(5, 10, 4)
    print(result)