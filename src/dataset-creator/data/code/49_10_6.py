import math
def is_positive(value: float) -> bool:
    return value > 0
if __name__ == '__main__':
    test_cases = [1, -5.5, 0, 3.14e-10]
    for num in test_cases:
        result = is_positive(num)
        print(f"Number {num} is positive: {result}")