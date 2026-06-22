import math

def cylinder_surface_area(height: float, radius: float) -> float:
    return 2 * math.pi * radius * height + 2 * math.pi * radius ** 2

if __name__ == '__main__':
    h = 10.0
    r = 5.0
    result = cylinder_surface_area(h, r)
    print(result)