import math

def compute_cylinder_areas(radius: float, height: float) -> tuple:
    lateral_area = 2 * math.pi * radius * height
    total_area = lateral_area + 2 * math.pi * radius ** 2
    return lateral_area, total_area

if __name__ == '__main__':
    radius = 5.0
    height = 10.0
    lateral, total = compute_cylinder_areas(radius, height)
    print(lateral)
    print(total)