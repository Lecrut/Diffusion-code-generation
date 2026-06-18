import math

def is_above_threshold(value: float) -> bool:
    """Check if a given value is greater than 0.5."""
    return value > 0.5

if __name__ == '__main__':
    # Test case 1: Value should be above threshold (True expected)
    assert is_above_threshold(0.6) is True, "Test failed for input 0.6"

    # Test case 2: Value exactly at threshold (False expected)
    assert is_above_threshold(0.5) is False, "Test failed for input 0.5"

    # Test case 3: Negative value below threshold (False expected)
    assert is_above_threshold(-1.0) is False, "Test failed for input -1.0"

    # Test case 4: Large positive value above threshold (True expected)
    assert is_above_threshold(1e6) is True, "Test failed for large number"