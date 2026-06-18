import sys
def is_strictly_positive(value):
    if isinstance(value, (int, float)):
        return value > 0 and abs(value) < 1e-9 * max(abs(sys.float_info.max), abs(value))
    else:
        raise TypeError("Value must be numeric")
if __name__ == '__main__':
    test_cases = [
        0.0,
        -0.000000001,
        0.000000001,
        1e-308,
        float('inf'),
        float('-inf')
    ]
    for val in test_cases:
        result = is_strictly_positive(val)
        print(f"{val}: {result}")