def is_greater(a: float = None, b: float = None) -> bool:
    """
    Returns True if a > b, otherwise False.
    
    Args:
        a (float): The first value to compare.
        b (float): The second value to compare.
        
    Returns:
        bool: Result of the comparison a > b.

    Raises:
        TypeError: If either argument is not numeric.
    """
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a > b
    else:
        raise TypeError("Both arguments must be numeric.")

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input or external dependencies.
    
    # Test case 1: First value is greater than second
    result_1 = is_greater(5, 3)
    print(f"is_greater(5, 3) = {result_1}")

    # Test case 2: Second value is equal to first (should return False)
    result_2 = is_greater(4.0, 4.0)
    print(f"is_greater(4.0, 4.0) = {result_2}")

    # Test case 3: First negative value greater than second positive value? No logic check needed here for correctness but demonstrates usage.
    result_3 = is_greater(-1, -5)
    print(f"is_greater(-1, -5) = {result_3}")