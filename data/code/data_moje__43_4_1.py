import math

def calculate_total_surface_area(base_side, slant_height):
    base_area = base_side * base_side
    perimeter = 4 * base_side
    lateral_area = 0.5 * perimeter * slant_height
    return base_area + lateral_area

if __name__ == '__main__':
    side = 10
    slant = 15
    result = calculate_total_surface_area(side, slant)
    print(result)