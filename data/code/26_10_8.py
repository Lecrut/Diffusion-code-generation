def is_greater(a: float | int, b: float | int) -> bool:
    """
    Returns True if 'a' is strictly greater than 'b', otherwise False.

    Args:
        a (float|int): The first numerical value to compare.
        b (float|int): The second numerical value to compare against.

    Returns:
        bool: True if a > b, False otherwise.
    """
    return a > b

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    sample_cases = [
        (10, 5),      # Expected: True
        (3.5, 4.2),   # Expected: False
        (-1, -5),     # Expected: True
        (7, 7),       # Expected: False
        (float('inf'), float('-inf')),  # Expected: True
    ]

    for i, (a_val, b_val) in enumerate(sample_cases):
        result = is_greater(a_val, b_val)
        expected = a_val > b_val
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {i + 1}: is_greater({a_val}, {b_val}) -> {result} (Expected: {expected}) [{status}]")