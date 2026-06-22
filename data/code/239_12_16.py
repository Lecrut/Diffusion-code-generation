def calculate_perimeter(length: float, width: float) -> float:
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative.")
    return 2 * (length + width)

if __name__ == '__main__':
    try:
        print(calculate_perimeter(10, 5))
    except ValueError as e:
        print(e)