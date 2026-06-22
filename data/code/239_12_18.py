def validate_dimensions(length: float, width: float) -> bool:
    return length > 0 and width > 0

def calculate_perimeter(length: float, width: float) -> float:
    if not validate_dimensions(length, width):
        raise ValueError("Length and width must be positive numbers")
    return 2 * (length + width)

if __name__ == '__main__':
    try:
        print(calculate_perimeter(5.0, 3.0))
    except ValueError as e:
        print(e)