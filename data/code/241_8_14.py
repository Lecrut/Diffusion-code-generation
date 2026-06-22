def validate_dimensions(length: int, width: int) -> bool:
    return length > 0 and width > 0

def calculate_area(length: int, width: int) -> int:
    if not validate_dimensions(length, width):
        raise ValueError("Both dimensions must be positive integers.")
    return length * width

if __name__ == '__main__':
    print(calculate_area(5, 10))
    print(calculate_area(3, 4))
    print(calculate_area(7, 2))
    print(calculate_area(10, 10))