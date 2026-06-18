def calculate_square_area(side_length: float) -> float:
    """
    Calculates the area of a square given its side length.
    
    The formula used is Area = side * side.
    
    Args:
        side_length (float): The length of one side of the square, must be non-negative.
        
    Returns:
        float: The calculated area of the square.
        
    Raises:
        ValueError: If the side length is negative.
    """
    if side_length < 0:
        raise ValueError("Side length cannot be negative.")
    
    return side_length * side_length

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [5.0, 10, -3]

    print("Area Calculator for Square")
    print("-" * 20)
    
    for side in test_cases:
        try:
            area = calculate_square_area(side)
            if side < 0:
                # This case should ideally raise an error based on docstring, 
                # but we handle it here to demonstrate the function's behavior.
                print(f"Side length {side} is invalid.")
            else:
                print(f"Side length: {side}")
                print(f"Area: {area:.2f}\n")
        except ValueError as e:
            print(f"Error for side {side}: {e}\n")