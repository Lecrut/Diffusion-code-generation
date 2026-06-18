def is_greater(a: float, b: float) -> bool:
    """Returns True if a > b, otherwise False."""
    return a > b

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input.
    result1 = is_greater(5, 3)
    assert result1 is True

    result2 = is_greater(4, 6)
    assert result2 is False

    print(f"is_greater(5, 3) = {result1}")
    print(f"is_greater(4, 6) = {result2}")