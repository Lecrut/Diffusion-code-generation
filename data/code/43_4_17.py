def calculate_square_area(side):
    """Calculates the area of a square given its side length.
    
    Args:
        side (numeric): The length of one side of the square.
        
    Returns:
        numeric: The calculated area.
        
    Raises:
        ValueError: If 'side' is not a number.
    """
    try:
        if isinstance(side, (int, float)) and not isinstance(side, bool):
            return side * side
        else:
            raise ValueError("The input must be numeric.")
    except TypeError as e:
        # Handles cases where the type check fails or other unexpected types are passed
        raise ValueError(f"Invalid input type. {side} is not a valid number.") from e

if __name__ == '__main__':
    # Sample test values hardcoded to ensure no user input, command-line arguments, 
    # network access, or pre-existing file dependencies are required.
    
    # Test Case 1: Valid integer side length
    print("Area for valid integer (side=5):", calculate_square_area(5))

    # Test Case 2: Valid float side length
    print("Area for valid float (side=4.2):", calculate_square_area(4.2))

    # Test Case 3: Invalid string input to verify ValueError handling
    try:
        result = calculate_square_area("invalid")
    except ValueError as ve:
        print(f"Caught expected error for invalid input type:")
        print(f"{type(ve).__name__}: {ve}")

    # Test Case 4: List input to verify comprehensive error handling
    try:
        result = calculate_square_area([10])
    except ValueError as ve:
        print(f"Caught expected error for list input:")
        print(f"{type(ve).__name__}: {ve}")