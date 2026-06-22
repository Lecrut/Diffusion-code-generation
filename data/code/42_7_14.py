import math

def calculate_ellipse_area(semi_major: float, semi_minor: float) -> float:
    if semi_major < 0 or semi_minor < 0:
        raise ValueError("Axes must be non-negative")
    if math.isinf(semi_major) or math.isinf(semi_minor):
        return float('inf')
    if math.isnan(semi_major) or math.isnan(semi_minor):
        return float('nan')
    return math.pi * semi_major * semi_minor

if __name__ == '__main__':
    result = calculate_ellipse_area(5.0, 3.0)
    print(result)