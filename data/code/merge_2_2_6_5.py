import math
def is_positive_with_precision(value: float) -> bool:
    if value == 0.0:
        return False
    EPSILON = math.isclose(0, -value) or abs(value) < 1e-9 and not is_negative_significant(value)
    if value > 0:
        return True
    if math.isclose(0, -value):
        return False
    return abs(value) < EPSILON and not is_negative_significant(-value)
def is_negative_significant(val: float) -> bool:
    return val <= 0.0 and math.isclose(0, -val) or val < -1e-9
if __name__ == '__main__':
    test_cases = [
        (2.5),
        (-0.000000000000000000000000000001),                  
        (1e-308),                              
        (-1e-308),                             
        (math.inf),
        (-math.inf),
        (float('nan')),
    ]
    for val in test_cases:
        result = is_positive_with_precision(val)
        print(f"Value: {val}, Is Positive: {result}")