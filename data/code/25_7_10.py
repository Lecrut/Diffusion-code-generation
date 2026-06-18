def contains_zero(numbers: list) -> bool:
    """
    Checks if the number zero exists within a given list of numbers.

    Args:
        numbers (list): A list containing numerical values.

    Returns:
        bool: True if 0 is present in the list, False otherwise.

    Time Complexity: O(n) where n is the length of the input list.
    Space Complexity: O(1).
    """
    return 0 in numbers

if __name__ == '__main__':
    # Sample test cases with no user interaction required
    sample_cases = [
        ([5, -2, 0, 3], True),
        ([-1.5, 0, "zero", 4], False),  # Note: string 'zero' is not the number 0
        ([0, 0, 0], True),
        ([], False),
        ([2, 4, 6, 8], False)
    ]

    for test_input, expected_output in sample_cases:
        result = contains_zero(test_input)
        status = "PASS" if result == expected_output else "FAIL"
        print(f"{status}: Input {test_input} -> Expected {expected_output}, Got {result}")