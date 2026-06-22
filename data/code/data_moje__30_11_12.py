import math

def validate_positive(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Radius must be a number")
    if value <= 0:
        raise ValueError("Radius must be positive")
    return value

def get_circle_area(radius):
    validated_radius = validate_positive(radius)
    return math.pi * validated_radius ** 2

if __name__ == '__main__':
    sample_radius = 5
    calculated_area = get_circle_area(sample_radius)
    print(calculated_area)