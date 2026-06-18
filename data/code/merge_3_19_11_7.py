def is_condition_true(a: any, b: any) -> bool:
    """
    Checks if two values 'a' and 'b' are equal using Python's built-in comparison operator.
    This leverages the optimized C implementation of '__eq__', which handles all data types efficiently.

    Args:
        a (any): The first value to compare.
        b (any): The second value to compare.

    Returns:
        bool: True if 'a' is equal to 'b', False otherwise.
    """
    return a == b

if __name__ == '__main__':
    # Hard-coded sample values for testing without any external input or files
    sample_a = 42
    sample_b = "Hello"

    result_true = is_condition_true(10, 10)
    result_false_equal_type = is_condition_true(sample_a, sample_b)
    result_false_diff_value = is_condition_true(5, 10)

    print(f"{result_true=}")      # Expected: True
    print(f"{result_false_equal_type=}")   # Expected: False (int vs str even if string was "42")
    print(f"{result_false_diff_value=}")     # Expected: False
    
    assert result_true is True, "Test 1 failed"
    assert result_false_equal_type is False, "Test 2 failed"
    assert result_false_diff_value is False, "Test 3 failed"

    print("All tests passed.")