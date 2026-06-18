import math

def is_greater_than_threshold(value: float, threshold: float = 10) -> bool:
    """Check if a given value is strictly greater than the predefined or provided threshold."""
    return value > threshold

if __name__ == '__main__':
    # Test case 1: Value less than default threshold (10)
    assert not is_greater_than_threshold(5), "Value should be considered NOT greater than 10"

    # Test case 2: Value equal to default threshold (10) - should return False because it's strictly greater
    assert not is_greater_than_threshold(10), "Equal value should be considered NOT greater than itself"

    # Test case 3: Value slightly above default threshold
    assert is_greater_than_threshold(10.01), "Value slightly above threshold should be True"

    # Test case 4: Large integer compared to float threshold (integers are comparable in Python)
    assert not is_greater_than_threshold(5, threshold=20), "Large int less than custom threshold should be False"

    # Test case 5: Negative value against positive threshold
    assert not is_greater_than_threshold(-1.5, threshold=-1), "Negative number smaller than -1 should be False"