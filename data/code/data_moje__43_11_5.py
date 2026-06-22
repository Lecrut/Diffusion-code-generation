import math

def compute_pyramid_surface_area(base_edge, height):
    slant_height = math.sqrt((base_edge / 2) ** 2 + height ** 2)
    base_area = base_edge ** 2
    lateral_area = 2 * base_edge * slant_height
    return base_area + lateral_area

if __name__ == '__main__':
    base = 10.0
    height_val = 12.0
    result = compute_pyramid_surface_area(base, height_val)
    print(result)