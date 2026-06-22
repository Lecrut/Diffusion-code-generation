import math

def calculate_cylinder_surface_area(radius, height):
    lateral_surface_area = 2 * math.pi * radius * height
    top_and_bottom_area = 2 * math.pi * radius ** 2
    return lateral_surface_area + top_and_bottom_area

if __name__ == '__main__':
    sample_radius = 5
    sample_height = 10
    result = calculate_cylinder_surface_area(sample_radius, sample_height)
    print(result)