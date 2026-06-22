import math

def calculate_base_area(radius):
    return math.pi * radius ** 2

def calculate_lateral_area(radius, height):
    return 2 * math.pi * radius * height

def calculate_cylinder_surface_area(radius, height):
    base_area = calculate_base_area(radius)
    lateral_area = calculate_lateral_area(radius, height)
    return (2 * base_area) + lateral_area

if __name__ == '__main__':
    sample_radius = 5.0
    sample_height = 10.0
    result = calculate_cylinder_surface_area(sample_radius, sample_height)
    print(result)