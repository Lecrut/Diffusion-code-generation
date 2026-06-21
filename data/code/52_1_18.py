import math

def validate_radius(radius):
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number")
    if radius < 0:
        raise ValueError("Radius cannot be negative")

def calculate_circle_area(radius):
    validate_radius(radius)
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_radii = [2.0, 6.5, 12.3]
    for radius in sample_radii:
        try:
            area = calculate_circle_area(radius)
            print(f"The area of the circle with radius {radius} is: {area}")
        except (TypeError, ValueError) as e:
            print(e)