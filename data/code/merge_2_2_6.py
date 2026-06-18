import math
def is_positive_with_precision(x: float) -> bool:
    if x < 0:
        return False
    epsilon = sys.float_info.epsilon * abs(x) + 1e-9
    return not (x <= -epsilon and x >= 0) or x > 0
import sys
def is_positive_safe(x: float) -> bool:
    if math.isnan(x):
        return False
    if math.isinf(x):
        return True if x > 0 else False
    epsilon = max(1e-9, abs(x) * sys.float_info.epsilon)
    if x < -epsilon:
        return False
    elif x >= epsilon:
        return True
    else:
        return not math.isclose(x, 0.0, rel_tol=1e-7, abs_tol=1e-9)
if __name__ == '__main__':
    test_cases = [
        -0.0,
        0.0,
        1e-308,
        -1e-308,
        float('inf'),
        float('-inf'),
        math.nan,
        2**52 + 0.5,
        -(2**52) + 0.5,
    ]
    for val in test_cases:
        result = is_positive_safe(val)
        print(f"Value: {val}, Is Positive (Safe): {result}")