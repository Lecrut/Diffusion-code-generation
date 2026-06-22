def calculate_perimeter(length: float, width: float) -> float:
    return 2 * (length + width)

if __name__ == '__main__':
    length = 10.0
    width = 5.0
    perimeter = calculate_perimeter(length, width)
    print(perimeter)