import math

def calculate_square_pyramid_surface_area(base_side, slant_height):
    base_area = base_side * base_side
    lateral_area = 2 * base_side * slant_height
    return base_area + lateral_area

if __name__ == '__main__':
    side = 4.0
    height = 6.0
    slant = math.sqrt((side / 2) ** 2 + height ** 2)
    result = calculate_square_pyramid_surface_area(side, slant)
    print(result)