def is_strictly_greater(number1: float | int, number2: float | int) -> bool:
    """
    Check if one number is strictly greater than another.

    Args:
        number1 (float | int): The first numeric value to compare.
        number2 (float | int): The second numeric value to compare against.

    Returns:
        bool: True if number1 > number2, False otherwise.

    Raises:
        TypeError: If either input is not a numerical type.
    """
    
    # Input validation for types
    if not isinstance(number1, (int, float)) or not isinstance(number2, (int, float)):
        raise TypeError(f"Both inputs must be numeric types (int or float). Received {type(number1).__name__} and {type(number2).__name__}.")

    # Perform the comparison safely. 
    # Note: Python's > operator handles standard numerical comparisons robustly for floats vs ints,
    # so direct comparison is safe after type validation above.
    return number1 > number2

if __name__ == '__main__':
    # Hard-coded sample values to test functionality without user interaction
    
    # Test Case 1: Normal case where first argument is greater
    result_1 = is_strictly_greater(5, 3)
    
    # Test Case 2: Equality (should return False)
    result_2 = is_strictly_greater(7.0, 7)
    
    # Test Case 3: Float less than Int
    result_3 = is_strictly_greater(4.5, 9)

    print(f"is_strictly_greater({5}, {3}) => {result_1}")       # Expected: True
    print(f"is_strictly_greater({7.0}, {7}) => {result_2}")     # Expected: False
    print(f"is_strictly_greater({4.5}, {9}) => {result_3}")   # Expected: False

    # Test Case 4: Error handling simulation (not executed as input is not interactive, 
    # but the function definition allows raising TypeError)
    try:
        result_err = is_strictly_greater("ten", "five")
    except TypeError as e:
        print(f"Error caught for invalid types: {e}")  # Expected error message printed