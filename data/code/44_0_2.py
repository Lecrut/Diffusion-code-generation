def calculate_rectangle_perimeter(length, width):
    if not isinstance(length, int) or not isinstance(width, int):
        raise TypeError("Inputs must be integers")
    if length <= 0 or width <= 0:
        raise ValueError("Inputs must be positive integers")
    return 2 * (length + width)

if __name__ == '__main__':
    print(calculate_rectangle_perimeter(5, 10))