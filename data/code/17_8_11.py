def is_even(n: int) -> bool:
    """Check if a number is even."""
    return n % 2 == 0

if __name__ == '__main__':
    # Test cases with hard-coded sample values including edge cases
    test_cases = [
        (0, True),      # Zero should be considered even
        (1, False),     # Positive odd number
        (-3, False),    # Negative odd number
        (2, True),      # Small positive even number
        (-4, True),     # Large negative even number
        (10**9 - 1, False), # Very large positive odd number
        -(10**9 + 1),   # Very large negative odd number
    ]

    passed_count = 0
    failed_cases = []

    for num, expected in test_cases:
        result = is_even(num)
        if result == expected:
            passed_count += 1
        else:
            failed_cases.append((num, expected, result))

    print(f"Tests run: {len(test_cases)}")
    print(f"Passed: {passed_count}")
    
    if failed_cases:
        print("Failed tests:")
        for num, exp, res in failed_cases:
            print(f"is_even({num}) = {res}, expected {exp}")
        
        # Exit with error code on failure so the module is truly testable as a unit
        exit(1)
    else:
        print("All tests passed.")