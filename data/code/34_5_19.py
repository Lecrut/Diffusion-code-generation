import math

def calculate_cylinder_surface_area(radius: float, height: float) -> float:
    base_area = math.pi * (radius ** 2)
    lateral_area = 2 * math.pi * radius * height
    return 2 * base_area + lateral_area

if __name__ == '__main__':
    radius = 5.0
    height = 10.0
    result = calculate_cylinder_surface_area(radius, height)
    print(result)