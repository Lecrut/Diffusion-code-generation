def cylinder_surface_area(radius: float, height: float) -> float:
    import math
    return 2 * math.pi * radius * (radius + height)

if __name__ == '__main__':
    print(cylinder_surface_area(5.0, 10.0))