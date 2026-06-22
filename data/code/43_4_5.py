import math

def total_surface_area(base_side, slant_height):
    base_area = base_side * base_side
    triangle_area = 0.5 * base_side * slant_height
    lateral_area = 4 * triangle_area
    return base_area + lateral_area

if __name__ == '__main__':
    result = total_surface_area(5.0, 10.0)
    print(result)