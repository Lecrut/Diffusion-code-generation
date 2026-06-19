import math

def validate_radius(radius):
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number")
    if radius < 0:
        raise ValueError("Radius cannot be negative")

def calculate_circle_area(radius):
    validate_radius(radius)
    return math.pi * radius**2

if __name__ == '__main__':
    test_cases = [
        (1, math.pi),
        (2, 4 * math.pi),
        (0, 0),
        (5, 25 * math.pi),
        (3.5, 12.25 * math.pi)
    ]
    for radius, expected in test_cases:
        result = calculate_circle_area(radius)
        print(f"Radius: {radius}, Area: {result}")