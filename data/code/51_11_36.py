import math

def validate_radius(radius):
    if not isinstance(radius, (int, float)):
        raise ValueError("Radius must be a number")
    if radius < 0:
        raise ValueError("Radius cannot be negative")

def calculate_circle_perimeter(radius):
    validate_radius(radius)
    return 2 * math.pi * radius

if __name__ == '__main__':
    try:
        radius = 12.5
        perimeter = calculate_circle_perimeter(radius)
        print(perimeter)
    except ValueError as e:
        print(e)