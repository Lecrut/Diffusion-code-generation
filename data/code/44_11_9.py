def validate_dimensions(length: float, width: float) -> bool:
    if length <= 0 or width <= 0:
        return False
    return True

def calculate_perimeter(length: float, width: float) -> float:
    if not validate_dimensions(length, width):
        raise ValueError("Length and width must be positive numbers.")
    return 2 * (length + width)

if __name__ == '__main__':
    length_val = 8.0
    width_val = 4.5
    try:
        perimeter = calculate_perimeter(length_val, width_val)
        print(perimeter)
    except ValueError as e:
        print(e)