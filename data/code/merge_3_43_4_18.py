def calculate_square_area(side):
    """
    Calculates the area of a square given its side length.
    
    Args:
        side (int | float): The length of one side of the square.
        
    Returns:
        int | float: The area of the square.
        
    Raises:
        ValueError: If 'side' is not an integer or float, or if it represents a negative number.
    """
    try:
        # Attempt to convert input to float first (covers both int and string representations)
        side = float(side)
        
        # Check for non-numeric inputs that might fail conversion but are handled by the try block above
        # If we reach here, 'side' is a valid number. However, if someone passes an object 
        # like a list or dict directly without string representation issues in Python's eval-like behavior,
        # float() will raise TypeError which we catch below as ValueError per task requirement logic for "non-numeric".
        
        # Re-evaluating the strict requirement: "handling potential non-numeric input gracefully by raising a ValueError"
        # The most robust way is to check type or attempt conversion and ensure only numeric types are accepted.
        
        if not isinstance(side, (int, float)) and not isinstance(side, str):
            raise ValueError("Input must be an integer or float.")
            
        side = float(side)  # Ensure it's a float for calculation
        
        if side < 0:
            raise ValueError("Side length cannot be negative.")
            
    except (TypeError, ValueError):
        # Catch cases where conversion fails due to non-numeric content in strings or invalid types
        raise ValueError(f"Invalid input type. Expected numeric value, got {type(side).__name__}.")

if __name__ == '__main__':
    # Sample test cases running without user interaction
    
    # Test 1: Valid integer side
    try:
        area = calculate_square_area(5)
        print(f"Area of square with side 5: {area}")
    except ValueError as e:
        print(f"Error for input 5: {e}")

    # Test 2: Valid float side
    try:
        area = calculate_square_area(3.14)
        print(f"Area of square with side 3.14: {area:.2f}")
    except ValueError as e:
        print(f"Error for input 3.14: {e}")

    # Test 3: String representation of number (should work if handled correctly, but let's test strict numeric check)
    try:
        area = calculate_square_area("7")
        print(f"Area of square with side '7': {area}")
    except ValueError as e:
        print(f"Error for input '7': {e}")

    # Test 4: Non-numeric string (should raise ValueError)
    try:
        area = calculate_square_area("hello")
        print(f"Area of square with side 'hello': {area}")
    except ValueError as e:
        print(f"Expected error for input 'hello': {e}")

    # Test 5: Negative number (should raise ValueError)
    try:
        area = calculate_square_area(-4)
        print(f"Area of square with side -4: {area}")
    except ValueError as e:
        print(f"Expected error for input -4: {e}")

    # Test 6: Invalid type (list, etc.)
    try:
        area = calculate_square_area([5])
        print(f"Area of square with side [5]: {area}")
    except ValueError as e:
        print(f"Expected error for input [5]: {e}")