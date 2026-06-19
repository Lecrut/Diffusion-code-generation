def calculate_square_area(side_length):
    """
    Calculate the area of a square given its side length.
    
    Args:
        side_length (float or int): The length of one side of the square.
        
    Returns:
        float: The calculated area of the square.
        
    Raises:
        ValueError: If the side length is negative.
    """
    if side_length < 0:
        raise ValueError("Side length cannot be negative.")
    
    return side_length ** 2

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or command-line arguments
    test_cases = [5.0, -3, "invalid", 10]

    print("Running square area calculator with hard-coded samples...")

    for side in test_cases:
        try:
            if isinstance(side, str):
                # Attempt to convert string input to float (simulating user error handling)
                numeric_side = float(side)
            else:
                numeric_side = side
            
            area = calculate_square_area(numeric_side)
            print(f"Side length: {numeric_side}, Area: {area}")

        except ValueError as ve:
            # Handle cases where input is invalid or negative
            if isinstance(side, str):
                print(f"Error processing '{side}': Could not convert to a valid number.")
            else:
                print(f"Error for side length {side}: {ve}")