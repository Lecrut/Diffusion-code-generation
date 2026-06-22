def calculate_cylinder_surface_area(radius, height):
    return 2 * 3.14159 * radius * (radius + height)

if __name__ == '__main__':
    radius_value = 3.0
    height_value = 5.0
    result = calculate_cylinder_surface_area(radius_value, height_value)
    print(result)