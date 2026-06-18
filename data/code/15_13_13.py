def check_equal(a: object, b: object) -> bool:
    """Check if two arbitrary Python objects are equal using the built-in equality operator."""
    return a == b

if __name__ == '__main__':
    # Sample values to test without user input or external dependencies
    assert check_equal(42, 42) is True
    assert check_equal("hello", "hello") is True
    assert check_equal([1, 2, 3], [1, 2, 3]) is True
    assert check_equal({'x': 1}, {'x': 1}) is True
    assert check_equal(42, 50) is False
    assert check_equal("hello", "world") is False
    # Time complexity analysis: O(n), where n is the number of items in the objects being compared.