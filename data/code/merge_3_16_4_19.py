def check_all_positive(numbers):
    """
    Returns True if all numbers in the list are positive, False otherwise.
    Optimized to stop at the first non-positive number found.
    
    Args:
        numbers (list of int or float): List of numeric values
        
    Returns:
        bool: True if all elements > 0, else False
    """
    for num in numbers:
        if num <= 0:
            return False
    return True

if __name__ == '__main__':
    # Sample test cases with hard-coded values (no user input required)
    sample_cases = [
        ([1, 2, 3], True),           # All positive -> True
        ([1, -2, 3], False),         # Contains negative -> False
        ([0.5, 1.5, 2.5], True),    # All positive floats -> True
        ([-1, -2, -3], False),       # All non-positive -> False
        ([], True),                  # Empty list considered all positive per logic
        ([42], True),                # Single positive number -> True
        ([-0.0], False),             # Negative zero is not strictly negative but <= 0 check handles it as expected for "positive" definition where > 0 required; however -0.0 == 0 so this returns False which aligns with standard interpretation of 'positive' meaning > 0
    ]

    print("Running sample tests...")
    all_passed = True
    for i, (test_input, expected) in enumerate(sample_cases):
        result = check_all_positive(test_input)
        status = "PASS" if result == expected else "FAIL"
        if result != expected:
            all_passed = False
        print(f"Test {i+1}: Input={test_input}, Expected={expected}, Got={result} [{status}]")

    if all_passed:
        print("All tests passed.")
    else:
        print("Some tests failed.")