def calculate_perimeter(length, width):
    if not isinstance(length, int) or not isinstance(width, int):
        raise ValueError("Length and width must be integers")
    return 2 * (length + width)

if __name__ == '__main__':
    length = 5
    width = 3
    print(calculate_perimeter(length, width))