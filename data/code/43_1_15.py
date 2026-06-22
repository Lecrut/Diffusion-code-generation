import math

def compute_pyramid_surface_area(base_edge, height):
    slant_height = math.sqrt((base_edge / 2) ** 2 + height ** 2)
    lateral_area = 2 * base_edge * slant_height
    base_area = base_edge ** 2
    total_area = base_area + lateral_area
    return {
        "lateral_surface_area": lateral_area,
        "total_surface_area": total_area
    }

if __name__ == '__main__':
    base_edge_value = 10
    height_value = 12
    results = compute_pyramid_surface_area(base_edge_value, height_value)
    print(results)