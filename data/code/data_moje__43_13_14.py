import math

def calculate_square_pyramid_surface_area(base_side, vertical_height):
    base_area = base_side ** 2
    slant_height = math.sqrt((base_side / 2) ** 2 + vertical_height ** 2)
    lateral_area = 4 * (0.5 * base_side * slant_height)
    total_surface_area = base_area + lateral_area
    return float(total_surface_area)

if __name__ == '__main__':
    base_side = 4.0
    vertical_height = 6.0
    result = calculate_square_pyramid_surface_area(base_side, vertical_height)
    print(result)