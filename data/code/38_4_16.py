import math

CONST_PI = math.pi
CONST_ONE_THIRD = 1 / 3

def validate_dimensions(radius, height):
    if radius <= 0:
        raise ValueError("Radius must be positive")
    if height <= 0:
        raise ValueError("Height must be positive")

def calculate_cone_volume(radius, height):
    validate_dimensions(radius, height)
    area_base = CONST_PI * (radius ** 2)
    volume = CONST_ONE_THIRD * area_base * height
    return volume

if __name__ == '__main__':
    sample_radius = 6
    sample_height = 9
    computed_volume = calculate_cone_volume(sample_radius, sample_height)
    print(computed_volume)