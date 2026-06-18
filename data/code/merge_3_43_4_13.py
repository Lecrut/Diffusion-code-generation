def calculate_square_area(side):
    """
    Calculates the area of a square given its side length.
    
    Args:
        side (int or float): The length of the square's side.
        
    Returns:
        int or float: The area of the square.
        
    Raises:
        ValueError: If the input is not numeric.
    """
    if not isinstance(side, (int, float)) or isinstance(side, bool):
        raise ValueError("Input must be a number.")
    
    return side ** 2

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    valid_cases = [4.5, 10]
    invalid_inputs = ["hello", None, True, {"side": 5}]
    
    print("Testing valid inputs:")
    for side in valid_cases:
        try:
            area = calculate_square_area(side)
            print(f"Side {side} -> Area {area}")
        except Exception as e:
            print(f"Error with input {side}: {e}")

    print("\nTesting invalid inputs:")
    for side in invalid_inputs:
        try:
            area = calculate_square_area(side)
            print(f"Side {side} -> Area {area}")
        except ValueError as e:
            print(f"Correctly raised error for input {side}: {e}")