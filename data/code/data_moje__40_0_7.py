def calculate_rectangular_box_surface_area(length, width, height):
    return 2 * (length * width + length * height + width * height)

if __name__ == '__main__':
    result = calculate_rectangular_box_surface_area(1, 2, 3)
    print(result)