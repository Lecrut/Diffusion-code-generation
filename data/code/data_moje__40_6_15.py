def calculate_rectangular_prism_surface_area(length, width, height):
    return 2 * (length * width + width * height + height * length)

if __name__ == '__main__':
    print(calculate_rectangular_prism_surface_area(3.0, 4.0, 5.0))