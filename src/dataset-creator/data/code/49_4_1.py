import sys
def is_strictly_positive(value):
    if isinstance(value, (int, float)):
        return value > 0 and abs(value) < 1e-9 * max(abs(1), abs(value))
    else:
        try:
            numeric_value = float(value)
            return numeric_value > 0 and abs(numeric_value) < 1e-9 * max(abs(1.0), abs(numeric_value))
        except (ValueError, TypeError):
            return False
if __name__ == '__main__':
    test_cases = [
        0.0000000001,
        -0.0000000001,
        0.0,
        1e-308,
        float('inf'),
        "invalid",
    ]
    for case in test_cases:
        result = is_strictly_positive(case)
        print(f"Input: {case!r}, Result: {result}")