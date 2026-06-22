import math

def validate_radius(radius):
    if radius <= 0:
        raise ValueError("Radius must be greater than zero")

def calculate_circle_perimeter(radius):
    validate_radius(radius)
    return 2 * math.pi * radius

if __name__ == '__main__':
    sample_radius = 10.5
    perimeter = calculate_circle_perimeter(sample_radius)
    print(perimeter)