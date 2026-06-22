import math

def validate_radius(radius):
    if not isinstance(radius, (int, float)):
        raise ValueError("Radius must be a number")
    if radius < 0:
        raise ValueError("Radius cannot be negative")

def calculate_area_circle(radius):
    validate_radius(radius)
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_radius = 7.5
    try:
        area = calculate_area_circle(sample_radius)
        print(area)
    except ValueError as e:
        print(e)