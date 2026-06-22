import math

def compute_pyramid_areas(base_edge, perpendicular_height):
    base_area = base_edge ** 2
    slant_height = math.sqrt((base_edge / 2) ** 2 + perpendicular_height ** 2)
    lateral_area = 2 * base_edge * slant_height
    total_area = lateral_area + base_area
    return {
        "lateral_area": lateral_area,
        "total_area": total_area
    }

if __name__ == '__main__':
    base_edge_value = 10.0
    height_value = 12.0
    results = compute_pyramid_areas(base_edge_value, height_value)
    print(results)