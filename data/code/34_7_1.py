from math import pi

def calculate_cylinder_surface_area(radius: float, height: float) -> float:
    return 2 * pi * radius * (radius + height)

if __name__ == '__main__':
    r = 5.0
    h = 10.0
    result = calculate_cylinder_surface_area(r, h)
    print(result)