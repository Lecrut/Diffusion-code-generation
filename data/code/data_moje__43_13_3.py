import math

def calculate_square_pyramid_surface_area(base_side, height):
    slant_height = math.sqrt((base_side / 2) ** 2 + height ** 2)
    base_area = base_side ** 2
    lateral_area = 2 * base_side * slant_height
    total_surface_area = base_area + lateral_area
    return total_surface_area

if __name__ == '__main__':
    base_side = 6
    height = 4
    result = calculate_square_pyramid_surface_area(base_side, height)
    print(result)