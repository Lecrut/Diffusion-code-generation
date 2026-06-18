def is_even(number: int) -> bool:
    """Check if a number is even.

    Args:
        number (int): The integer to check.

    Returns:
        bool: True if the number is even, False otherwise.
    """
    return number % 2 == 0

if __name__ == '__main__':
    # Test cases covering edge cases: zero, positive numbers, and negative numbers.
    
    test_cases = [
        (0, True),      # Zero is even
        (1, False),     # Smallest positive odd integer
        (-1, False),    # Smallest negative odd integer
        (2, True),      # Small positive even number
        (-2, True),     # Small negative even number
        (100, True),    # Large positive even number
        (-100, True),   # Large negative even number
        (999999999, False)  # Very large odd number
    ]

    passed_count = 0
    
    print("Running test cases for is_even function:")
    
    for input_val, expected in test_cases:
        result = is_even(input_val)
        status = "PASS" if result == expected else "FAIL"
        
        if result == expected:
            passed_count += 1
        
        # Print detailed output only on failure to keep standard stream clean or always
        print(f"is_even({input_val}) -> {result} (Expected: {expected}) [{status}]")

    print("\nTotal tests run:", len(test_cases))
    print("Tests passed:", passed_count)
    
    if passed_count == len(test_cases):
        print("All tests passed successfully.")