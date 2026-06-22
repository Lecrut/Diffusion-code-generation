import math

def cylinder_surface_area(radius: float, height: float) -> float:
    return 2 * math.pi * radius * (radius + height)

if __name__ == '__main__':
    r = 5.0
    h = 10.0
    area = cylinder_surface_area(r, h)
    print(area)