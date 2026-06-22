def validate_length_and_width(length, width):
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        raise ValueError("Both length and width must be numeric.")
    if length <= 0 or width <= 0:
        raise ValueError("Both length and width must be positive numbers.")

def calculate_perimeter(length, width):
    validate_length_and_width(length, width)
    return 2 * (length + width)

if __name__ == '__main__':
    sample_length = 5
    sample_width = 3
    print(f"Perimeter of rectangle with length {sample_length} and width {sample_width}: {calculate_perimeter(sample_length, sample_width)}")

    try:
        calculate_perimeter(-1, 3)
    except ValueError as e:
        print(f"Error for invalid input: {e}")

    try:
        calculate_perimeter(5, "three")
    except ValueError as e:
        print(f"Error for invalid input: {e}")