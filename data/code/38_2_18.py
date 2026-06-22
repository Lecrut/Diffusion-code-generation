import math

def _validate_cone_parameters(radius, height):
    if radius <= 0 or height <= 0:
        raise ValueError("Radius and height must be positive numbers")
    if not isinstance(radius, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Radius and height must be numeric types")

def calculate_cone_volume(radius, height):
    _validate_cone_parameters(radius, height)
    area_base = math.pi * radius * radius
    volume = (area_base * height) / 3.0
    return volume

if __name__ == '__main__':
    target_radius = 3
    target_height = 7
    result = calculate_cone_volume(target_radius, target_height)
    print(result)