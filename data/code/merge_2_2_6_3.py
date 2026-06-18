import math
def is_positive_with_precision(value: float) -> bool:
    return value > 0 and not (math.isinf(value) or math.isnan(value))
if __name__ == '__main__':
    test_cases = [
        1.5,
        -2.3,
        float('inf'),
        float('-inf'),
        float('nan'),
        0.0 + 1e-294 * (math.copysign(1, math.inf)),
    ]
    for val in test_cases:
        result = is_positive_with_precision(val)
        print(f"Value: {val}, Is Positive: {result}")