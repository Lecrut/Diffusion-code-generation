import math

def calculate_cylinder_areas(radius, height):
    lateral_area = 2 * math.pi * radius * height
    total_area = 2 * math.pi * radius * (radius + height)
    return lateral_area, total_area

if __name__ == '__main__':
    radius = 5
    height = 10
    lateral, total = calculate_cylinder_areas(radius, height)
    print(lateral, total)