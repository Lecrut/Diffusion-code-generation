import math

def validate_radius(radius):
    if not isinstance(radius, (int, float)) or radius <= 0:
        raise ValueError("Radius must be a positive number")

def calculate_circle_perimeter(radius):
    validate_radius(radius)
    return 2 * math.pi * radius

if __name__ == '__main__':
    sample_radius = 5.0
    print(calculate_circle_perimeter(sample_radius))