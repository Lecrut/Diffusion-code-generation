def calculate_square_area(side_length):
    """
    Calculates the area of a square given its side length.
    
    Parameters:
        side_length (float or int): The length of one side of the square. Must be non-negative.
        
    Returns:
        float: The calculated area of the square.
        
    Raises:
        ValueError: If the side length is negative.
        TypeError: If the input type is not a number.
    """
    if not isinstance(side_length, (int, float)):
        raise TypeError("Side length must be an integer or float.")
    
    if side_length < 0:
        raise ValueError("Side length cannot be negative.")
        
    return side_length ** 2

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    test_cases = [5, -3, "invalid", None]

    print("Running square area calculator with hard-coded samples.\n")

    for case in test_cases:
        try:
            if isinstance(case, str):
                # Attempting to parse string as float/int (simulating input conversion)
                side = float(case)
            else:
                side = case
            
            area = calculate_square_area(side)
            print(f"Input: {case} -> Area: {area}")

        except ValueError as ve:
            print(f"Error for input '{case}': {ve}")
        except TypeError as te:
            print(f"Type error for input '{case}': {te}")