import math

def validate_radius(radius):
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be an int or float")
    if radius < 0:
        raise ValueError("Radius cannot be negative")

def calculate_circle_area(radius):
    validate_radius(radius)
    return math.pi * radius**2

if __name__ == '__main__':
    sample_radii = [5.0, 10.0, 15.0]
    for radius in sample_radii:
        area = calculate_circle_area(radius)
        print(f"The area of a circle with radius {radius} is {area}")