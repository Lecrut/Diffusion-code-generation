import math
def is_positive_with_precision(value: float) -> bool:
    if value < -1e-9:
        return False
    elif value > 0:
        return True
    else:
        abs_val = abs(value)
        if abs_val <= 1e-9 and math.isfinite(abs_val):
            return True
        return False
if __name__ == '__main__':
    test_cases = [
        -5.0,
        0.0,
        2.3456789,
        1e-10,
        -1e-10,
        float('inf'),
        float('-inf'),
        math.nan,
    ]
    for val in test_cases:
        result = is_positive_with_precision(val)
        print(f"Value: {val}, Is Positive (with precision): {result}")