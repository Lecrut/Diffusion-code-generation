def calculate_surface_area(length, width, height):
    if length <= 0 or width <= 0 or height <= 0:
        raise ValueError('Dimensions must be positive numbers.')
    return 2 * (length * width + width * height + height * length)
if __name__ == '__main__':
    length_val = 5.0
    width_val = 3.0
    height_val = 2.0
    area = calculate_surface_area(length_val, width_val, height_val)
    print(area)