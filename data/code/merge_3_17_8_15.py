def is_even(number: int) -> bool:
    """Check if a given integer is even."""
    return number % 2 == 0

if __name__ == '__main__':
    # Test cases with hard-coded sample values covering edge cases.
    test_cases = [
        (0, True),      # Zero should be considered even
        (-4, True),     # Negative even numbers
        (-3, False),    # Negative odd numbers
        (1, False),     # Positive odd numbers
        (2, True),      # Small positive even number
        (987654, True)  # Large even number
    ]

    all_passed = True
    for input_val, expected in test_cases:
        result = is_even(input_val)
        if result != expected:
            print(f"Test failed for {input_val}: expected {expected}, got {result}")
            all_passed = False
    
    if all_passed:
        print("All tests passed.")