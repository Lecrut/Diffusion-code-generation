import math

def calculate_cylinder_surface_area(radius: float, height: float) -> float:
    return 2 * math.pi * radius * height + 2 * math.pi * radius ** 2

if __name__ == '__main__':
    radius = 5.0
    height = 10.0
    area = calculate_cylinder_surface_area(radius, height)
    print(area)