def calculate_square_area(side):
    """Calculate the area of a square given its side length."""
    if isinstance(side, (int, float)):
        return side * side
    raise ValueError("Side must be numeric.")

if __name__ == '__main__':
    # Sample test cases without user input
    try:
        result = calculate_square_area(5)
        print(f"Area for side 5 is {result}")

        result2 = calculate_square_area(-3.0)
        print(f"Area for side -3.0 is {result2}")
        
        # Test non-numeric input gracefully (will raise ValueError as expected)
        try:
            result_error = calculate_square_area("invalid")
        except ValueError as e:
            print(f"Caught expected error for invalid input: {e}")

    except Exception as e:
        print(f"Unexpected error occurred: {e}")