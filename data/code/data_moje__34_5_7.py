def calculate_cylinder_surface_area(radius, height):
    return 2 * 3.14159 * radius * (radius + height)

if __name__ == '__main__':
    radius = 5
    height = 10
    area = calculate_cylinder_surface_area(radius, height)
    print(area)