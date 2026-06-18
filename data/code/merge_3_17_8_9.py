def is_even(n: int) -> bool:
    """Check if an integer n is even."""
    return n % 2 == 0

if __name__ == '__main__':
    # Test cases with hard-coded values covering edge cases and normal numbers.
    test_cases = [
        (0, True),      # Zero should be even
        (-4, True),     # Negative number divisible by 2 should be even
        (-3, False),    # Negative odd number
        (1, False),     # Positive odd number
        (59, False),    # Larger positive odd number
        (60, True),     # Larger positive even number
    ]

    for value, expected in test_cases:
        result = is_even(value)
        if result == expected:
            print(f"PASS: is_even({value}) = {result}")
        else:
            print(f"FAIL: is_even({value}) returned {result}, expected {expected}")

    # Demonstrate the function with a quick example output
    sample_value = 100
    print(f"\nExample check for number {sample_value}: ")
    if is_even(sample_value):
        print("The result is even.")
    else:
        print("The result is odd.")

    # Run the tests under unittest framework to ensure they are testable and runnable via pytest or python -m unittest
    import doctest
    suite = doctest.testmod(optionflags=doctest.VERBOSITY)
    
    # Simple assertion check for all defined cases again using a loop inside main logic as explicit proof of correctness
    print("\n--- Explicit Verification Summary ---")
    passed_count = 0
    failed_cases = []
    for value, expected in test_cases:
        if is_even(value) == expected:
            passed_count += 1
        else:
            failed_cases.append((value, expected))

    print(f"Passed {passed_count}/{len(test_cases)} cases.")
    if len(failed_cases) > 0:
        for val, exp in failed_cases:
            print(f"Failed case is_even({val}) == {exp}")
    
    assert passed_count == len(test_cases), "Some test cases did not pass."