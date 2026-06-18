def is_above_threshold(value: float) -> bool:
    """Check if a given value exceeds the predefined threshold of 50.0."""
    THRESHOLD = 50.0
    return value > THRESHOLD

if __name__ == '__main__':
    # Example test cases with hard-coded sample values
    assert is_above_threshold(60) is True, "Expected true for input greater than threshold"
    assert is_above_threshold(49.9) is False, "Expected false for input less than threshold"
    assert is_above_threshold(50.0) is False, "Expected false for input equal to threshold"
    print("All assertions passed.")