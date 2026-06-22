import math

def square_pyramid_surface_area(base_side, vertical_height):
    slant_height = math.sqrt((base_side / 2) ** 2 + vertical_height ** 2)
    base_area = base_side ** 2
    lateral_area = 2 * base_side * slant_height
    return base_area + lateral_area

if __name__ == '__main__':
    base_side = 10
    vertical_height = 12
    result = square_pyramid_surface_area(base_side, vertical_height)
    print(result)