def calculate_rectangle_perimeter(length, width):
    if not (isinstance(length, int) and length > 0 and isinstance(width, int) and width > 0):
        raise ValueError("Length and width must be positive integers.")
    return 2 * (length + width)
if __name__ == '__main__':
    length_val = 10
    width_val = 5
    perimeter = calculate_rectangle_perimeter(length_val, width_val)
    print(perimeter)