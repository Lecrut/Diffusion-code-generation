from numbers import Number
def is_positive(value: Number) -> bool:
    return value > 0
if __name__ == '__main__':
    test_cases = [1, -5, 0.0, float('inf'), float('-inf')]
    for case in test_cases:
        print(f"{case}: {is_positive(case)}")