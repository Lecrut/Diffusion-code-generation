import math

def is_above_threshold(value: float) -> bool:
    """Check if a given value is greater than 100."""
    return value > 100

if __name__ == '__main__':
    # Test case 1: Value clearly above threshold
    assert is_above_threshold(250.5), "Value should be above threshold"

    # Test case 2: Value exactly at threshold (should fail)
    assert not is_above_threshold(100.0), "Threshold value should not pass check"

    # Test case 3: Negative value below threshold
    assert not is_above_threshold(-50), "Negative values should be below threshold"

    # Test case 4: Float slightly above integer threshold
    assert is_above_threshold(100.0001), "Value just above threshold should pass"