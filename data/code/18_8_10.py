def is_above_threshold(value: float) -> bool:
    """Check if a given value is greater than 100."""
    return value > 100

if __name__ == '__main__':
    # Test case 1: Value less than threshold should be False
    assert not is_above_threshold(50), "Expected False for input 50"

    # Test case 2: Value equal to threshold should be False (strictly greater)
    assert not is_above_threshold(100.0), "Expected False for input 100.0"

    # Test case 3: Value slightly above threshold should be True
    assert is_above_threshold(100.01), "Expected True for input 100.01"

    # Test case 4: Large value should be True
    assert is_above_threshold(999999), "Expected True for large positive number"

    print("All tests passed.")