import math

def calculate_pyramid_surface_area(base_side, height):
    slant_height = math.sqrt((base_side / 2) ** 2 + height ** 2)
    base_area = base_side ** 2
    lateral_area = 2 * base_side * slant_height
    return base_area + lateral_area

if __name__ == '__main__':
    base = 4.0
    h = 6.0
    result = calculate_pyramid_surface_area(base, h)
    print(result)