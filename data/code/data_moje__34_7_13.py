import math

def calculate_cylinder_surface_area(radius: float, height: float) -> float:
    base_area = math.pi * radius ** 2
    lateral_area = 2 * math.pi * radius * height
    total_surface_area = 2 * base_area + lateral_area
    return total_surface_area

if __name__ == '__main__':
    r = 5.0
    h = 10.0
    area = calculate_cylinder_surface_area(r, h)
    print(area)