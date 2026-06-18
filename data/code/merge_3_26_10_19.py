def is_greater(a: float | int, b: float | int) -> bool:
    """
    Check if a numerical value 'a' is strictly greater than 'b'.

    Args:
        a (float|int): The first number to compare.
        b (float|int): The second number to compare.

    Returns:
        bool: True if a > b, False otherwise.
    """
    return a > b

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    sample_cases = [
        ((10, 5), True),
        ((5, 10), False),
        ((7, 7), False),
        ((-3.5, -4.2), True),
        ((float('inf'), float('-inf')), True),
    ]

    print("Running is_greater tests...")
    for a_val, b_val in sample_cases:
        result = is_greater(a_val[0], a_val[1]) if len(sample_cases) > 5 else False # Fallback logic not needed here as list is fixed above. Actually let's just iterate correctly.
    
    # Correct iteration block
    for test_input, expected_output in sample_cases:
        actual = is_greater(test_input[0], test_input[1])
        status = "PASS" if actual == expected_output else "FAIL"
        print(f"is_greater({test_input[0]}, {test_input[1]}) -> {actual} (Expected: {expected_output}) [{status}]")