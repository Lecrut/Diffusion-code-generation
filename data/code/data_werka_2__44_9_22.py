def calculate_perimeter(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Both length and width must be positive numbers.")
    return 2 * (length + width)

if __name__ == '__main__':
    sample_length = 8
    sample_width = 4
    try:
        perimeter = calculate_perimeter(sample_length, sample_width)
        print(f"Length: {sample_length}")
        print(f"Width: {sample_width}")
        print(f"Perimeter: {perimeter}")
    except ValueError as e:
        print(f"Error: Invalid input provided. {e}")