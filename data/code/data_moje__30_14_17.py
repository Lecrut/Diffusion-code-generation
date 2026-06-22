import math

def calculate_circle_area(radius: float) -> float:
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return math.pi * radius * radius

if __name__ == '__main__':
    sample_radii = [0, 1, 2.5, 10, 100]
    for r in sample_radii:
        area = calculate_circle_area(r)
        print(area)