import math

def compute_cylinder_surface_area(radius, height):
    lateral_area = 2 * math.pi * radius * height
    base_area = math.pi * radius * radius
    return 2 * base_area + lateral_area

if __name__ == '__main__':
    sample_radius = 5
    sample_height = 10
    total_surface_area = compute_cylinder_surface_area(sample_radius, sample_height)
    print(total_surface_area)