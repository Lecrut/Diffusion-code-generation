import sys
def is_strictly_positive(value):
    epsilon = 1e-9
    return value > epsilon
if __name__ == '__main__':
    test_cases = [0.5, -2.3, 1e-10, 0, -1e-10]
    for case in test_cases:
        result = is_strictly_positive(case)
        print(f"{case}: {result}")