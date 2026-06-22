import math

def calculate_circle_area(radius: float) -> float:
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return math.pi * radius * radius

if __name__ == "__main__":
    test_radiuses = [1.0, 2.5, 0.0]
    for r in test_radiuses:
        print(calculate_circle_area(r))