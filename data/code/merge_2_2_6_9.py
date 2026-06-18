import math
def is_positive_with_precision(value: float) -> bool:
    if value < -1e-9:
        return False
    elif value > 0:
        return True
    else:
        abs_val = abs(value)
        if abs_val <= 1e-9 and math.isfinite(abs_val):
            return False
        return True
if __name__ == '__main__':
    test_cases = [
        -5.0,
        0.0,
        2.3456789,
        float('inf'),
        float('-inf'),
        math.nan,
        1e-100,
        -1e-100,
    ]
    for val in test_cases:
        result = is_positive_with_precision(val)
        print(f"Value: {val}, Is Positive (with precision): {result}")