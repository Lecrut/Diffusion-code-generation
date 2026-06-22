def calculate_rectangle_perimeter(length: int, width: int) -> int:
    return 2 * (length + width)

if __name__ == '__main__':
    length = 5
    width = 3
    print(calculate_rectangle_perimeter(length, width))