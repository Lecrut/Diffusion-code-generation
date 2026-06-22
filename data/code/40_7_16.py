def calculate_rectangular_box_surface_area(length, width, height):
    return 2 * (length * width + width * height + height * length)

if __name__ == '__main__':
    length = 5
    width = 3
    height = 4
    surface_area = calculate_rectangular_box_surface_area(length, width, height)
    print(surface_area)