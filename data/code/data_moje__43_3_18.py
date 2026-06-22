import math

def calculate_square_pyramid_surface_area(base_side, perpendicular_height):
    if base_side <= 0 or perpendicular_height <= 0:
        raise ValueError("Base side and perpendicular height must be positive")
    base_area = base_side ** 2
    slant_height = math.sqrt((base_side / 2) ** 2 + perpendicular_height ** 2)
    lateral_area = 2 * base_side * slant_height
    return base_area + lateral_area

if __name__ == '__main__':
    sample_base_side = 4.0
    sample_perpendicular_height = 3.0
    result = calculate_square_pyramid_surface_area(sample_base_side, sample_perpendicular_height)
    print(result)