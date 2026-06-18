import sys
def is_positive(value: float) -> bool:
    return value > 0
if __name__ == '__main__':
    test_cases = [42, -15.7, 3e-8, 0]
    for case in test_cases:
        result = is_positive(case)
        print(f"Input: {case}, Is Positive: {result}")