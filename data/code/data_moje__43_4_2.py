import math

def total_surface_area(base_side, slant_height):
    base_area = base_side ** 2
    lateral_area = 4 * (base_side * slant_height) / 2
    return base_area + lateral_area

if __name__ == '__main__':
    base_side_value = 10
    slant_height_value = 12
    result = total_surface_area(base_side_value, slant_height_value)
    print(result)