def calculate_rectangle_perimeter(length: int, width: int) -> int:
    if not isinstance(length, int) or length <= 0:
        raise ValueError("Length must be a positive integer")
    if not isinstance(width, int) or width <= 0:
        raise ValueError("Width must be a positive integer")
    return 2 * (length + width)

if __name__ == '__main__':
    result = calculate_rectangle_perimeter(5, 10)
    print(result)