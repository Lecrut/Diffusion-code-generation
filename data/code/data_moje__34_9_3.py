import math

def calculate_cylinder_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

if __name__ == '__main__':
    RADIUS = 5
    HEIGHT = 10
    result = calculate_cylinder_surface_area(RADIUS, HEIGHT)
    print(result)