import math

def total_surface_area(base_side, slant_height):
    base_area = base_side * base_side
    lateral_area = 2 * base_side * slant_height
    return base_area + lateral_area

if __name__ == '__main__':
    base_side = 10
    slant_height = 15
    result = total_surface_area(base_side, slant_height)
    print(result)