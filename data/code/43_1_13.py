import math

def calculate_pyramid_areas(base_edge, height):
    half_base = base_edge / 2.0
    slant_height = math.sqrt(height ** 2 + half_base ** 2)
    lateral_area = base_edge * slant_height
    total_area = lateral_area + base_edge ** 2
    return {
        "lateral_area": lateral_area,
        "total_area": total_area
    }

if __name__ == '__main__':
    base_edge_value = 10.0
    height_value = 12.0
    result = calculate_pyramid_areas(base_edge_value, height_value)
    print(result)