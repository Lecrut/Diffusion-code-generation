def validate_dimensions(length: int, width: int) -> bool:
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive integers.")
    return True

def calculate_area(length: int, width: int) -> int:
    validate_dimensions(length, width)
    return length * width

if __name__ == '__main__':
    print(calculate_area(5, 10))
    print(calculate_area(3, 4))
    print(calculate_area(7, 2))
    print(calculate_area(10, 10))