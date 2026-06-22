import math

def cylinder_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

if __name__ == '__main__':
    result = cylinder_surface_area(5, 10)
    print(result)