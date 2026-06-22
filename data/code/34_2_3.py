import math

def calculate_cylinder_areas(radius: float, height: float):
    lateral_area = 2 * math.pi * radius * height
    total_area = 2 * math.pi * radius * (radius + height)
    return lateral_area, total_area

if __name__ == '__main__':
    radius_value = 5.0
    height_value = 10.0
    lateral, total = calculate_cylinder_areas(radius_value, height_value)
    print(lateral)
    print(total)