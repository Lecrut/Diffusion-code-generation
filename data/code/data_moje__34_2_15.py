import math

def calculate_cylinder_areas(radius, height):
    lateral_area = 2 * math.pi * radius * height
    total_area = 2 * math.pi * radius * (radius + height)
    return lateral_area, total_area

if __name__ == '__main__':
    sample_radius = 5
    sample_height = 10
    lat_area, tot_area = calculate_cylinder_areas(sample_radius, sample_height)
    print(lat_area)
    print(tot_area)