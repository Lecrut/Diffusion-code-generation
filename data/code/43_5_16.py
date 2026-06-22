import math

def calculate_square_pyramid_surface_area(base_side, height):
    base_area = base_side * base_side
    slant_height = math.sqrt((base_side / 2) ** 2 + height ** 2)
    lateral_area = 4 * (0.5 * base_side * slant_height)
    return base_area + lateral_area

if __name__ == '__main__':
    side = 5
    h = 12
    result = calculate_square_pyramid_surface_area(side, h)
    print(result)