import math

def cylinder_surface_area(radius, height):
    return 2 * math.pi * radius * height + 2 * math.pi * radius ** 2

if __name__ == '__main__':
    radius = 5
    height = 10
    area = cylinder_surface_area(radius, height)
    print(area)