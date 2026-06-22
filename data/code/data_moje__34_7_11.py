import math

def cylinder_surface_area(radius: float, height: float) -> float:
    return 2 * math.pi * radius * (radius + height)

if __name__ == '__main__':
    radius = 5.0
    height = 10.0
    area = cylinder_surface_area(radius, height)
    print(area)