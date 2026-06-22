import math

def compute_square_pyramid_surface_area(base_side, slant_height):
    base_area = base_side ** 2
    lateral_area = 2 * base_side * slant_height
    total_surface_area = base_area + lateral_area
    return total_surface_area

if __name__ == '__main__':
    base_side_value = 4
    slant_height_value = 5
    result = compute_square_pyramid_surface_area(base_side_value, slant_height_value)
    print(result)