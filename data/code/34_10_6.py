import math

def calculate_cylinder_surface_area(radius: float, height: float) -> float:
    area = 2 * math.pi * radius * (radius + height)
    return area

if __name__ == '__main__':
    radius = 5
    height = 10
    result = calculate_cylinder_surface_area(radius, height)
    print(result)