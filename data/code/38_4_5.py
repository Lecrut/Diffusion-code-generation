import math

def validate_dimensions(radius, height):
    if radius <= 0:
        raise ValueError("Radius must be positive.")
    if height <= 0:
        raise ValueError("Height must be positive.")
    return True

def calculate_cone_volume(radius, height):
    validate_dimensions(radius, height)
    base_area = math.pi * (radius ** 2)
    volume = base_area * height
    return volume / 3

if __name__ == '__main__':
    radius_val = 6
    height_val = 9
    computed_volume = calculate_cone_volume(radius_val, height_val)
    print(computed_volume)