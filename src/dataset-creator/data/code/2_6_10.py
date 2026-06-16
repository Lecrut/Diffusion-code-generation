import math
def is_positive_with_precision(value: float) -> bool:
    if value > 0 and not (math.isinf(value) or math.isnan(value)):
        return True
    return False
if __name__ == '__main__':
    test_cases = [1e-324, -1.7976931348623157e+308, 0.0, float('inf'), float('-inf')]
    for val in test_cases:
        result = is_positive_with_precision(val)
        print(f"Value {val}: Is positive? {result}")