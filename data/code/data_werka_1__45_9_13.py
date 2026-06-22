import math

PI = 3.141592653589793

def validate_radius(radius):
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number")
    if radius < 0:
        raise ValueError("Radius cannot be negative")

def calculate_circle_area(radius):
    validate_radius(radius)
    return PI * radius ** 2

if __name__ == '__main__':
    sample_radius = 10.0
    area = calculate_circle_area(sample_radius)
    print(area)