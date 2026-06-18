def is_positive(number: float) -> bool:
    """
    Returns True if number is strictly greater than zero, False otherwise.
    
    Args:
        number (float): The numerical argument to check.
        
    Returns:
        bool: True if number > 0, else False.
    """
    return number > 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [1.5, -3.2, 0, float('inf'), float('-inf')]
    
    results = []
    for val in test_cases:
        result = is_positive(val)
        results.append((val, result))
        
    # Print results to verify functionality (no interactive input required)
    print("Testing is_positive function:")
    for value, expected_result in results:
        status = "PASS" if expected_result == (value > 0) else "FAIL"
        print(f"is_positive({value}) -> {expected_result} [{status}]")