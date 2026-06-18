import math
def check_positive(value):
    return value > 0
if __name__ == '__main__':
    test_cases = [1, -5, 3.14, float('-inf'), float('inf'), 0]
    for case in test_cases:
        result = check_positive(case)
        print(f"Input: {case}, Result: {result}")