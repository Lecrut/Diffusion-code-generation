def calculate_square_area(side_length):
    """Calculate the area of a square using direct multiplication."""
    return side_length * side_length

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed.
    test_cases = [5, 0.75, -3]

    for length in test_cases:
        area = calculate_square_area(length)
        print(f"Area of a square with side {length}: {area}")