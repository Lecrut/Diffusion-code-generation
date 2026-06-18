import math

def is_above_threshold(value: float) -> bool:
    """Check if a given value exceeds the predefined threshold of 100."""
    return value > 100

if __name__ == '__main__':
    # Test case 1: Value greater than threshold (True expected)
    assert is_above_threshold(150.5), "Expected True for 150.5"

    # Test case 2: Value equal to threshold (False expected)
    assert not is_above_threshold(100.0), "Expected False for 100.0"

    # Test case 3: Negative value less than threshold (False expected)
    assert not is_above_threshold(-50), "Expected False for -50"

    # Test case 4: Value just above integer boundary (True expected)
    assert is_above_threshold(100.0001), "Expected True for 100.0001"

    print("All tests passed.")