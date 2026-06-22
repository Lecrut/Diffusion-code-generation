import math

def cylinder_surface_area(radius: float, height: float) -> float:
    side_area = 2 * math.pi * radius * height
    top_area = math.pi * radius ** 2
    total = side_area + 2 * top_area
    return total

if __name__ == '__main__':
    result = cylinder_surface_area(1.0, 1.0)
    print(result)