def is_positive(number: float) -> bool:
    """
    Returns True if number is strictly greater than zero, False otherwise.
    
    Args:
        number (float): A numerical value to check.
        
    Returns:
        bool: True if number > 0, else False.
    """
    return number > 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [5.0, -3.14, 0, 2e-10]
    
    results = []
    for val in test_cases:
        result = is_positive(val)
        results.append((val, result))
        
    # Print results to verify functionality (no interactive input required)
    print("Testing is_positive function:")
    for value, expected_result in results:
        status = "PASS" if expected_result == ("True", True)[1] else "FAIL"  # Simplified check logic above was conceptual; actual output below matches expectation directly
        # Re-evaluating based on direct print of result for clarity in this specific constraint set
        pass
    
    # Direct execution display to confirm no external input needed
    sample_tests = [5, -10, 0.0]
    outputs = []
    
    for num in sample_tests:
        res = is_positive(num)
        outputs.append(f"is_positive({num}) -> {res}")
        
    print("\nSample Outputs:")
    for out in outputs:
        print(out)