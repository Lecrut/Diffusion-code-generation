import math

def cylinder_surface_area(radius: float, height: float) -> float:
    lateral_area = 2 * math.pi * radius * height
    base_area = math.pi * radius ** 2
    total_area = lateral_area + 2 * base_area
    return total_area

if __name__ == '__main__':
    result = cylinder_surface_area(5, 10)
    print(result)