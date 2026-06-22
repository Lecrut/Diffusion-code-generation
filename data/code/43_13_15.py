import math

def surface_area_square_pyramid(base_side, height):
    slant_height = math.sqrt((base_side / 2) ** 2 + height ** 2)
    base_area = base_side ** 2
    lateral_area = 2 * base_side * slant_height
    return base_area + lateral_area

if __name__ == '__main__':
    side = 6
    h = 4
    result = surface_area_square_pyramid(side, h)
    print(result)