import math

def calculate_cylinder_surface_area(radius, height):
    lateral_surface_area = 2 * math.pi * radius * height
    base_area = math.pi * radius ** 2
    total_surface_area = lateral_surface_area + 2 * base_area
    return total_surface_area

if __name__ == '__main__':
    sample_radius = 5.0
    sample_height = 10.0
    result = calculate_cylinder_surface_area(sample_radius, sample_height)
    print(result)