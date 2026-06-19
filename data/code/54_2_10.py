import math

def validate_radius(radius):
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number")
    if radius < 0:
        raise ValueError("Radius cannot be negative")

def get_area(radius):
    validate_radius(radius)
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_values = [3.5, 7.0, 10.2]
    for value in sample_values:
        area = get_area(value)
        print(f"The area of the circle with radius {value} is: {area}")