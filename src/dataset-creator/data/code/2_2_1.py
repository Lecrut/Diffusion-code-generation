import sys
def is_positive(value):
    return (isinstance(value, (int, float)) and value > 0)
if __name__ == '__main__':
    test_cases = [1.5, -3, 0, "hello", None]
    for case in test_cases:
        result = is_positive(case)
        print(f"Input: {case}, Is Positive: {result}")