def calculate_surface_area(length, width, height):
    if length <= 0 or width <= 0 or height <= 0:
        raise ValueError('Dimensions must be positive numbers')
    return 2 * (length * width + width * height + height * length)
if __name__ == '__main__':
    length = 5.0
    width = 3.0
    height = 4.0
    surface_area = calculate_surface_area(length, width, height)
    print(surface_area)