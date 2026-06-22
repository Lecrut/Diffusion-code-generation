import math

def calculate_square_pyramid_surface_area(base_side, vertical_height):
    slant_height = math.sqrt((base_side / 2) ** 2 + vertical_height ** 2)
    base_area = base_side ** 2
    lateral_area = 2 * base_side * slant_height
    return base_area + lateral_area

if __name__ == '__main__':
    sample_base_side = 4.0
    sample_vertical_height = 6.0
    result = calculate_square_pyramid_surface_area(sample_base_side, sample_vertical_height)
    print(result)