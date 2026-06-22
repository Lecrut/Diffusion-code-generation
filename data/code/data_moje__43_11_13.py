import math

def compute_square_pyramid_surface_area(base_edge, height):
    base_area = base_edge * base_edge
    slant_height = math.sqrt((base_edge / 2) ** 2 + height ** 2)
    lateral_area = 4 * (0.5 * base_edge * slant_height)
    return base_area + lateral_area

if __name__ == '__main__':
    base_edge = 5.0
    height = 8.0
    area = compute_square_pyramid_surface_area(base_edge, height)
    print(area)