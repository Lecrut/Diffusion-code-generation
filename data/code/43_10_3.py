def calculate_square_area(side_length):
    """Calculate the area of a square given its side length."""
    return side_length ** 2

if __name__ == '__main__':
    # Sample block to run without user input, command-line arguments, network access, or pre-existing files.
    
    test_cases = [5]

    for value in test_cases:
        try:
            area_value = calculate_square_area(value)
            print(f"Side length: {value}")
            print(f"Area of square: {area_value}\n")
        except Exception as e:
            print(f"Error calculating area for side {value}: {e}")

    # Optional interactive prompt simulation based on task requirements, though input() is restricted by the 'Never call input()' rule.
    # Since the requirement states "Do not include... any interactive prompt", we omit user-facing prompts entirely and rely solely on the sample block above to demonstrate functionality without requiring runtime interaction or system inputs.