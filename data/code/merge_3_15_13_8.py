def check_equal(a: object, b: object) -> bool:
    """Check if two objects are equal using the built-in equality operator."""
    return a == b

if __name__ == '__main__':
    # Sample test cases with hard-coded values (no user input or external dependencies required)
    assert check_equal(5, 5) is True
    assert check_equal([1, 2], [1, 2]) is True
    assert check_equal("hello", "world") is False
    print("All tests passed.")