def calculate_rectangular_box_surface_area(length, width, height):
    return 2 * (length * width + length * height + width * height)

if __name__ == '__main__':
    length = 5
    width = 10
    height = 15
    result = calculate_rectangular_box_surface_area(length, width, height)
    print(result)