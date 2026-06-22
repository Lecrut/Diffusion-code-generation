import math

def compute_square_pyramid_areas(base_edge, height):
    if base_edge <= 0 or height <= 0:
        raise ValueError('Base edge and height must be positive.')
    base_area = base_edge ** 2
    slant_height = math.sqrt((base_edge / 2) ** 2 + height ** 2)
    lateral_area = 0.5 * (4 * base_edge) * slant_height
    total_area = base_area + lateral_area
    return {'lateral_area': lateral_area, 'total_area': total_area}
if __name__ == '__main__':
    base_edge = 5.0
    height = 6.0
    result = compute_square_pyramid_areas(base_edge, height)
    print(result)