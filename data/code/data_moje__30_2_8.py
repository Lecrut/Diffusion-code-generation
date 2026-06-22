import math

def calculate_circle_area(radius: float) -> float:
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

if __name__ == '__main__':
    test_radius_1 = 5.0
    test_radius_2 = 0.0
    print(calculate_circle_area(test_radius_1))
    print(calculate_circle_area(test_radius_2))