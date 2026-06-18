def is_positive(number):
    """
    Returns True if number is strictly greater than zero, False otherwise.
    
    Args:
        number (int or float): The numerical value to check.
        
    Returns:
        bool: True if number > 0, else False.
    """
    return number > 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    test_cases = [1, -5, 0.0, 3.14, float('inf'), float('-inf')]
    
    results = []
    for val in test_cases:
        result = is_positive(val)
        results.append((val, result))
    
    # Print results to verify functionality (no external dependencies needed)
    print("Testing is_positive function:")
    for value, expected_result in results:
        status = "PASS" if expected_result == True else "FAIL"
        print(f"is_positive({value}) -> {expected_result} [{status}]")