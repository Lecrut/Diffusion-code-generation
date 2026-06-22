import math

def calculate_cylinder_areas(radius, height):
    pi = math.pi
    lateral_surface_area = 2 * pi * radius * height
    total_surface_area = 2 * pi * radius * (radius + height)
    return lateral_surface_area, total_surface_area

if __name__ == '__main__':
    sample_radius = 5
    sample_height = 10
    lateral, total = calculate_cylinder_areas(sample_radius, sample_height)
    print(f"Lateral Surface Area: {lateral}")
    print(f"Total Surface Area: {total}")