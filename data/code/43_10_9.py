def calculate_square_area(side_length):
    """
    Calculate the area of a square given its side length.
    
    Parameters:
        side_length (float or int): The length of one side of the square.
        
    Returns:
        float: The calculated area of the square.
    """
    return side_length ** 2

def main():
    # Hard-coded sample values to ensure execution without user input, 
    # command-line arguments, network access, or pre-existing files.
    test_cases = [5, -3.0, "10", None]

    for i, value in enumerate(test_cases):
        try:
            if isinstance(value, str) and not value.lstrip('-').isdigit():
                # Simulate potential non-numeric input error handling logic 
                # by attempting conversion directly as the task implies user interaction context.
                side = float(value)
            else:
                side = float(value)

            area = calculate_square_area(side)
            
            if value is None or not isinstance(value, (int, float)):
                print(f"Test case {i + 1}: Invalid input provided.")
            else:
                print(f"Square with side length {side} has an area of {area}")

        except ValueError as ve:
            # Gracefully handle cases where conversion to float fails
            if isinstance(value, str):
                print(f"Test case {i + 1}: Error - '{value}' is not a valid number.")
            else:
                print(f"Test case {i + 1}: Unexpected error occurred while processing input of type {type(value).__name__}.")

if __name__ == '__main__':
    main()