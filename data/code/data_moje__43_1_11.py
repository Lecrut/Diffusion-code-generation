import math

def calculate_pyramid_area(base_edge, height):
    slant_height = math.sqrt((base_edge / 2)**2 + height**2)
    base_area = base_edge ** 2
    lateral_area = base_edge * base_edge * math.sqrt(2) / 2 * (slant_height / height) * 2
    lateral_area = base_edge * math.sqrt((base_edge / 2)**2 + height**2) * 2
    total_area = base_area + lateral_area
    return {
        "base_area": base_area,
        "lateral_area": lateral_area,
        "total_area": total_area,
        "slant_height": slant_height
    }

if __name__ == '__main__':
    base_edge_value = 6
    height_value = 8
    result = calculate_pyramid_area(base_edge_value, height_value)
    print(result)