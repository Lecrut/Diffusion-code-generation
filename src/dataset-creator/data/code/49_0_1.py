import math
def is_positive(value):
    return isinstance(value, (int, float)) and value > 0
if __name__ == '__main__':
    test_cases = [10, -5.5, 0, 3.999, "invalid", None]
    for case in test_cases:
        result = is_positive(case) if isinstance(case, (int, float)) else False
        print(f"Input: {case} -> Is Positive: {result}")