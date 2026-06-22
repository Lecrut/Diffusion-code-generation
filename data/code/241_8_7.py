def validate_input(length: int, width: int) -> bool:
    if not isinstance(length, int) or not isinstance(width, int):
        return False
    if length < 0 or width < 0:
        return False
    return True

def calculate_area(length: int, width: int) -> int:
    if validate_input(length, width):
        return length * width
    else:
        raise ValueError("Invalid input values")

if __name__ == '__main__':
    print(calculate_area(5, 10))
    print(calculate_area(3, 4))
    print(calculate_area(7, 2))
    print(calculate_area(10, 10))