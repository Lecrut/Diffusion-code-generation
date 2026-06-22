import math

def _validate_dimensions(radius, height):
    if radius <= 0 or height <= 0:
        raise ValueError("Dimensions must be positive numbers")
    return True

def cone_volume(radius, height):
    _validate_dimensions(radius, height)
    base_area = math.pi * radius ** 2
    return (1 / 3) * base_area * height

if __name__ == '__main__':
    sample_radius = 4
    sample_height = 12
    computed_volume = cone_volume(sample_radius, sample_height)
    print(computed_volume)