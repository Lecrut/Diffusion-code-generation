import math

def calculate_square_pyramid_surface_area(base_side, vertical_height):
    base_area = base_side ** 2
    slant_height = math.sqrt((base_side / 2) ** 2 + vertical_height ** 2)
    lateral_area = 4 * (0.5 * base_side * slant_height)
    return base_area + lateral_area

if __name__ == '__main__':
    result = calculate_square_pyramid_surface_area(4, 5)
    print(result)