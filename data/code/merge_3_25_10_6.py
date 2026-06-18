def is_zero(value):
    """
    Returns True if the input value is exactly zero, False otherwise.
    
    Args:
        value (number): A numerical argument to check.
        
    Returns:
        bool: True if value == 0, else False.
    """
    return value == 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        (0, True),
        (-1e-308, False),  # Near-zero but not exactly zero (float)
        (0.0, True),       # Explicit float zero
        (int(0), True),    # Integer zero
        (1/2 - 0.5 + 0.49999999999999994, False), # Float arithmetic result close to zero but not exact
        ([], False),       # Non-numerical input handled by equality check safely for robustness in this context
    ]

    print("Running 'is_zero' function tests...")
    all_passed = True
    
    for i, (input_val, expected) in enumerate(test_cases):
        result = is_zero(input_val)
        status = "PASS" if result == expected else "FAIL"
        if result != expected:
            all_passed = False
        print(f"Test {i+1}: input={repr(input_val)}, expected={expected}, got={result} -> [{status}]")

    if all_passed:
        print("\nAll tests passed.")
    else:
        print("\nSome tests failed.")