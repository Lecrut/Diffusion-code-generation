import math

def is_value_greater_than_threshold(value: float) -> bool:
    """Check if a given value exceeds the predefined threshold of 100.0."""
    return value > 100.0

if __name__ == '__main__':
    test_cases = [
        (95, False),   # Below threshold
        (100, False),  # Equal to threshold
        (100.01, True),# Just above threshold
        (math.inf, True),     # Infinity is greater than threshold
    ]

    for value in test_cases:
        result = is_value_greater_than_threshold(value)
        assert isinstance(result, bool), "Result must be a boolean"
    
    print("All tests passed.")