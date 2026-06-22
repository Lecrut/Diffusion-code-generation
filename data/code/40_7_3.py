def calculate_rectangular_box_surface_area(length, width, height):
    if length <= 0 or width <= 0 or height <= 0:
        return 0.0
    return 2 * (length * width + width * height + height * length)

if __name__ == '__main__':
    length = 3.0
    width = 4.0
    height = 5.0
    result = calculate_rectangular_box_surface_area(length, width, height)
    print(result)