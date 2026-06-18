def contains_zero(numbers):
    """
    Checks if the number zero exists within a list of numbers.

    Args:
        numbers (list[int]): A list containing integers or floats to check.

    Returns:
        bool: True if 0 is in the list, False otherwise.

    Time Complexity: O(n) where n is the length of the input list.
    Space Complexity: O(1).
    """
    return any(num == 0 for num in numbers)

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    sample_lists = [
        [1, -2, 0, 3],       # Expected: True (contains zero)
        [5, 7, 9, 11],      # Expected: False (no zero)
        [-0.0, 1.5],        # Expected: True (-0.0 == 0 is True in Python)
        [],                  # Expected: False (empty list)
    ]

    for i, test_list in enumerate(sample_lists):
        result = contains_zero(test_list)
        print(f"Test case {i + 1}: List={test_list}, Contains Zero? {result}")