def calculate_cylinder_surface_area(radius, height):
    import math
    return 2 * math.pi * radius * (radius + height)

if __name__ == '__main__':
    r = 3.0
    h = 5.0
    result = calculate_cylinder_surface_area(r, h)
    print(result)