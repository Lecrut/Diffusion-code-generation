def is_different(a: int, b: int) -> bool:
    """Yields True if two input numbers are different, False otherwise."""
    yield a != b

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    results = list(is_different(5, 10))      # Expected: [True]
    assert results[0] is True

    results = list(is_different(3, 3))       # Expected: [False]
    assert results[0] is False

    print("All tests passed.")