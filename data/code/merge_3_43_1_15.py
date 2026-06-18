def calculate_square_area(side):
    """Calculate the area of a square given its side length."""
    return side * side

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    test_cases = [5.0, 10, 3]

    for case in test_cases:
        area = calculate_square_area(case)
        print(f"Side length {case}: Area is {area}")