import math

BASE_FACES = 1
TRIANGLE_FACES = 4
HALF = 0.5

def compute_surface_area(base_side, vertical_height):
    half_base = base_side * HALF
    slant_height = math.sqrt((base_side * half_base) + (vertical_height * vertical_height))
    triangle_area = (base_side * slant_height) * HALF
    total_lateral_area = triangle_area * TRIANGLE_FACES
    base_area = base_side * base_side
    return total_lateral_area + base_area

if __name__ == '__main__':
    s = 10.0
    h = 12.0
    area = compute_surface_area(s, h)
    print(area)