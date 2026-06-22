import math

def surface_area_square_pyramid(base_side, slant_height):
    base_area = base_side ** 2
    lateral_area = 2 * base_side * slant_height
    total_area = base_area + lateral_area
    return total_area

if __name__ == '__main__':
    base_side_value = 10
    slant_height_value = 12
    result = surface_area_square_pyramid(base_side_value, slant_height_value)
    print(result)