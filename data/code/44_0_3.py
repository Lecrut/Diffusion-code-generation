def calculate_rectangle_perimeter(length, width):
    if not isinstance(length, int) or length <= 0:
        raise ValueError("Length must be a positive integer.")
    if not isinstance(width, int) or width <= 0:
        raise ValueError("Width must be a positive integer.")
    return 2 * (length + width)

if __name__ == '__main__':
    l_val = 10
    w_val = 5
    print(calculate_rectangle_perimeter(l_val, w_val))