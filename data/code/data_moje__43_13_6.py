import math

def calculate_square_pyramid_surface_area(base_side, vertical_height):
    base_area = base_side * base_side
    slant_height = math.sqrt((base_side / 2) ** 2 + vertical_height ** 2)
    lateral_area = 2 * base_side * slant_height
    total_surface_area = base_area + lateral_area
    return total_surface_area

if __name__ == '__main__':
    base = 4.0
    height = 3.0
    result = calculate_square_pyramid_surface_area(base, height)
    print(result)