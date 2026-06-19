def calculate_square_area(side_length):
    """
    Calculate the area of a square given its side length.
    
    Parameters:
        side_length (float or int): The length of one side of the square.
        
    Returns:
        float: The calculated area of the square.
    """
    return side_length ** 2

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    test_cases = [5, -3.0]

    for value in test_cases:
        try:
            area = calculate_square_area(value)
            print(f"Area of square with side {value}: {area}")
        except Exception as e:
            # Graceful error handling for invalid inputs or unexpected errors
            print(f"Error calculating area for input {value}: {e}")

    # Note: The task requires prompting the user, but also forbids calling input() 
    # and interactive prompts. This block demonstrates calculation with hard-coded values 
    # as per the specific constraint "Include an if __name__ == '__main__': block with hard-coded sample values."