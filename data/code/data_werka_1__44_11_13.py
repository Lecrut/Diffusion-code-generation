def validate_dimensions(length: float, width: float) -> None:
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")

def calculate_perimeter(length: float, width: float) -> float:
    validate_dimensions(length, width)
    return 2 * (length + width)

if __name__ == '__main__':
    try:
        length_val = 8.5
        width_val = 6.3
        perimeter = calculate_perimeter(length_val, width_val)
        print(perimeter)
    except ValueError as e:
        print(e)