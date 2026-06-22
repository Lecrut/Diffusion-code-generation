import math

def calculate_slant_height(base_side, perpendicular_height):
    if base_side <= 0 or perpendicular_height <= 0:
        raise ValueError("Base side and perpendicular height must be positive.")
    half_side = base_side / 2.0
    return math.sqrt(half_side ** 2 + perpendicular_height ** 2)

def calculate_square_pyramid_surface_area(base_side, perpendicular_height):
    if base_side <= 0 or perpendicular_height <= 0:
        raise ValueError("Base side and perpendicular height must be positive.")
    slant_height = calculate_slant_height(base_side, perpendicular_height)
    base_area = base_side ** 2
    lateral_area = 4 * (0.5 * base_side * slant_height)
    return base_area + lateral_area

if __name__ == '__main__':
    base = 10.0
    height = 12.0
    area = calculate_square_pyramid_surface_area(base, height)
    print(area)