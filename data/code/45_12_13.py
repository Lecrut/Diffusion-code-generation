import math

def validate_radius(radius):
    if not isinstance(radius, (int, float)):
        raise ValueError("Radius must be a number.")
    if radius < 0:
        raise ValueError("Radius cannot be negative.")

def calculate_circle_area(radius):
    validate_radius(radius)
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_radii = [5, 10.5]
    for radius in sample_radii:
        area = calculate_circle_area(radius)
        print(f"Area of circle with radius {radius}: {area}")