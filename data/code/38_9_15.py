import math

def validate_positive(value, name):
    if value <= 0:
        raise ValueError(f"{name} must be positive")
    return value

def calculate_cone_volume(radius, height):
    r = validate_positive(radius, "radius")
    h = validate_positive(height, "height")
    base_area = math.pi * r ** 2
    volume = (1 / 3) * base_area * h
    return volume

if __name__ == '__main__':
    sample_radius = 10
    sample_height = 20
    computed_volume = calculate_cone_volume(sample_radius, sample_height)
    print(computed_volume)