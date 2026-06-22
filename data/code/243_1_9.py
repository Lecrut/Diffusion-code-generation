import math

def validate_radius(radius):
    if radius < 0:
        raise ValueError("Radius must be a non-negative number")

def calculate_circumference(radius):
    validate_radius(radius)
    circumference = 2 * math.pi * radius
    return circumference

if __name__ == '__main__':
    sample_radius = 5.0
    result = calculate_circumference(sample_radius)
    print(result)