import math

def validate_radius(radius):
    if not isinstance(radius, (int, float)) or radius <= 0:
        raise ValueError("Radius must be a positive number")
    return radius

def calculate_circumference(radius):
    validated_radius = validate_radius(radius)
    circumference = 2 * math.pi * validated_radius
    return circumference

if __name__ == '__main__':
    sample_radius = 5.0
    result = calculate_circumference(sample_radius)
    print(result)