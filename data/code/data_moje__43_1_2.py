import math

def pyramid_areas(base_edge, height):
    if base_edge <= 0 or height <= 0:
        raise ValueError('Dimensions must be positive')
    slant_height = math.sqrt((base_edge / 2) ** 2 + height ** 2)
    lateral_area = 2 * base_edge * slant_height
    base_area = base_edge ** 2
    total_area = base_area + lateral_area
    return {'base_edge': base_edge, 'height': height, 'lateral_area': lateral_area, 'total_area': total_area}
if __name__ == '__main__':
    base_edge_value = 10
    height_value = 12
    result = pyramid_areas(base_edge_value, height_value)
    print(result)