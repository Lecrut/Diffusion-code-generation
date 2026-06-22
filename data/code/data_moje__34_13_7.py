import math

def cylinder_surface_area(radius: float, height: float) -> float:
    base_area = math.pi * radius * radius
    lateral_area = 2 * math.pi * radius * height
    return 2 * base_area + lateral_area

if __name__ == '__main__':
    result = cylinder_surface_area(5, 10)
    print(result)