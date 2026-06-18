def is_greater(a: float, b: float) -> bool:
    """Returns True if a > b, otherwise False."""
    return a > b

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    result1 = is_greater(5.0, 3.0)
    assert result1 is True

    result2 = is_greater(4.0, 7.0)
    assert result2 is False

    print(f"is_greater(5.0, 3.0) = {result1}")
    print(f"is_greater(4.0, 7.0) = {result2}")