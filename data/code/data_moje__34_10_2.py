import math

def cylinder_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

if __name__ == '__main__':
    radius = 3
    height = 5
    area = cylinder_surface_area(radius, height)
    print(area)