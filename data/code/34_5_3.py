import math

def cylinder_surface_area(radius, height):
    area = 2 * math.pi * radius * (radius + height)
    return area

if __name__ == '__main__':
    radius = 3
    height = 5
    result = cylinder_surface_area(radius, height)
    print(result)