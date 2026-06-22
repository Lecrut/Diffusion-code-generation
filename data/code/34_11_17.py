import math

def compute_cylinder_areas(radius, height):
    lateral_area = 2 * math.pi * radius * height
    total_area = 2 * math.pi * radius * (radius + height)
    return lateral_area, total_area

if __name__ == '__main__':
    radius = 5.0
    height = 10.0
    lateral_area, total_area = compute_cylinder_areas(radius, height)
    print(lateral_area)
    print(total_area)