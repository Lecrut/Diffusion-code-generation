def calculate_rectangle_perimeter(width, height):
    return 2 * (width + height)

if __name__ == '__main__':
    width_val = 7
    height_val = 3
    perimeter = calculate_rectangle_perimeter(width_val, height_val)
    print(perimeter)