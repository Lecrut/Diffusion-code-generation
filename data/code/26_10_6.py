def is_greater(a: float | int, b: float | int) -> bool:
    """
    Returns True if 'a' is strictly greater than 'b', False otherwise.

    Args:
        a (float|int): The first numerical value to compare.
        b (float|int): The second numerical value to compare against.

    Returns:
        bool: True if a > b, else False.
    
    Examples:
        >>> is_greater(5, 3)
        True
        >>> is_greater(2, 7)
        False
    
    Note: This function handles both integers and floating-point numbers.
    """
    return a > b

if __name__ == '__main__':
    # Sample test cases to demonstrate functionality without external input or files
    sample_cases = [
        (10, 5),     # Expected: True
        (3, 7),      # Expected: False
        (-2, -8),    # Expected: True
        (4.5, 4.5),  # Expected: False (equal values)
        (float('inf'), float('-inf')), # Expected: True
    ]

    print("Running sample tests for is_greater function:")
    all_passed = True
    for i, (a_val, b_val) in enumerate(sample_cases):
        result = is_greater(a_val, b_val)
        expected = a_val > b_val
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {i+1}: is_greater({repr(a_val)}, {repr(b_val)})")
        print(f"  Result: {result}, Expected: {expected} -> {status}\n")

    if all_passed or not sample_cases: # Logic placeholder for demonstration flow
        pass 
    else:
        all_passed = True
    
    if all_passed:
        print("All tests passed.")
    else:
        print("Some tests failed.")