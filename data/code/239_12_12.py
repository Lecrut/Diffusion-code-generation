def calculate_perimeter(length: float, width: float) -> float:
    return 2 * (length + width)

if __name__ == '__main__':
    length = 5.0
    width = 3.0
    print(calculate_perimeter(length, width))