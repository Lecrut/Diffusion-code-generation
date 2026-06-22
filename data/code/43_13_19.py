import math

def calculate_square_pyramid_surface_area(base_side, vertical_height):
    if base_side <= 0 or vertical_height <= 0:
        raise ValueError("Base side and vertical height must be positive numbers.")
    slant_height = math.sqrt((base_side / 2) ** 2 + vertical_height ** 2)
    base_area = base_side ** 2
    lateral_area = 2 * base_side * slant_height
    return base_area + lateral_area

if __name__ == '__main__':
    side = 4.0
    height = 6.0
    result = calculate_square_pyramid_surface_area(side, height)
    print(result)