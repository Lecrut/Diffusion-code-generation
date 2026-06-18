import math
def is_positive(value: float) -> bool:
    return value > 0
if __name__ == '__main__':
    test_cases = [1.5, -3.2, 0, 4e-8]
    for case in test_cases:
        result = is_positive(case)
        print(f"{case} -> {result}")