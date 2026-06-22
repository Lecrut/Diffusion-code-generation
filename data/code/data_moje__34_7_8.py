import math

def calculate_cylinder_surface_area(radius: float, height: float) -> float:
    lateral_area = 2 * math.pi * radius * height
    base_area = math.pi * radius ** 2
    total_area = lateral_area + 2 * base_area
    return total_area

if __name__ == '__main__':
    sample_radius = 5.0
    sample_height = 10.0
    result = calculate_cylinder_surface_area(sample_radius, sample_height)
    print(result)