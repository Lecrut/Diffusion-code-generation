import math

def validate_radius(radius):
    if not isinstance(radius, (int, float)):
        raise ValueError("Radius must be a number")
    if radius < 0:
        raise ValueError("Radius cannot be negative")

def get_area(radius):
    validate_radius(radius)
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_radius = 5.0
    area_result = get_area(sample_radius)
    print(area_result)