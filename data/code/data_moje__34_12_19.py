def calculate_cylinder_surface_area(radius, height):
    if radius < 0 or height < 0:
        raise ValueError("Radius and height must be non-negative.")
    return 2 * 3.141592653589793 * radius * (radius + height)

if __name__ == '__main__':
    r = 5
    h = 10
    result = calculate_cylinder_surface_area(r, h)
    print(result)