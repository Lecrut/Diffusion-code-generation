def check_equal(a: object, b: object) -> bool:
    """Checks if two arbitrary Python objects are equal using the built-in equality operator."""
    return a == b

if __name__ == '__main__':
    # Sample test cases with hard-coded values (no user input or external dependencies required)
    assert check_equal(5, 5) is True
    assert check_equal([1, 2], [3, 4]) is False
    assert check_equal((1,), {"a": "b"}) is False
    print("All basic equality checks executed successfully.")