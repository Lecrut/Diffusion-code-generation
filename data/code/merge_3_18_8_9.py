import math

def is_above_threshold(value: float) -> bool:
    """Check if a given value is strictly greater than 100."""
    return value > 100

if __name__ == '__main__':
    # Test case 1: Value above threshold should be True
    assert is_above_threshold(150.5) is True, "Test failed for input 150.5"

    # Test case 2: Value exactly at threshold should be False (not strictly greater)
    assert is_above_threshold(100.0) is False, "Test failed for input 100.0"

    # Test case 3: Negative value below threshold should be False
    assert is_above_threshold(-50.0) is False, "Test failed for input -50.0"

    # Test case 4: Zero below threshold should be False
    assert is_above_threshold(0.0) is False, "Test failed for input 0.0"