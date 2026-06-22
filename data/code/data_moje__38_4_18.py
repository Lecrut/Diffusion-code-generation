import math

def is_valid_dimension(value, name):
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a number")
    if value <= 0:
        raise ValueError(f"{name} must be positive")
    return True

def calculate_cone_volume(radius, height):
    is_valid_dimension(radius, "radius")
    is_valid_dimension(height, "height")
    area_base = math.pi * radius * radius
    volume = area_base * height / 3.0
    return volume

if __name__ == '__main__':
    r = 6
    h = 9
    result = calculate_cone_volume(r, h)
    print(result)