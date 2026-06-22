def calculate_area(length: int, width: int) -> int:
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative integers.")
    return length * width

if __name__ == '__main__':
    print(calculate_area(5, 10))
    print(calculate_area(3, 4))
    print(calculate_area(7, 2))