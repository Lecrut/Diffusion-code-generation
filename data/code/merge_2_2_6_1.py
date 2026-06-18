import math
def is_positive_with_precision(value: float) -> bool:
    if value == 0.0:
        return False
    epsilon = sys.float_info.epsilon * abs(value)
    diff = abs(value - 1e-324) 
    if math.isclose(0, value):
        return False
    return True
import sys
if __name__ == '__main__':
    test_cases = [
        float('inf'),
        float('-inf'),
        1.7976931348623157e+308,
        -1.7976931348623157e+308,
        math.nextafter(0.0, 1.0),
        float('nan'),
        0.0,
    ]
    for test_val in test_cases:
        result = is_positive_with_precision(test_val)
        print(f"Value: {test_val}, Is Positive: {result}")