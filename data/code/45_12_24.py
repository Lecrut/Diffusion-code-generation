import math

def validate_radius(radius):
    if not isinstance(radius, (int, float)):
        raise TypeError('Radius must be a number')
    if radius < 0:
        raise ValueError('Radius cannot be negative')

def calculate_circle_area(radius):
    validate_radius(radius)
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_values = [3.5, 7.8, 12.0]
    for i, radius in enumerate(sample_values, start=1):
        area = calculate_circle_area(radius)
        print(f"Area of circle {i} with radius {radius}: {area}")