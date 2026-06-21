import math

def validate_radius(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Radius must be a numeric type")
    if value < 0:
        raise ValueError("Radius must be non-negative")
    return value

def compute_area(radius):
    validated_radius = validate_radius(radius)
    return math.pi * (validated_radius ** 2)

if __name__ == '__main__':
    _radius = 5
    _result = compute_area(_radius)
    print(_result)