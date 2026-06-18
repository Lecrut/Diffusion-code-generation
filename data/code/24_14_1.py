import math

def is_negative(n: int) -> bool:
    return n < 0 if isinstance(n, (int, float)) else False

if __name__ == '__main__':
    test_cases = [-5, -1, 0, 1, 2]
    for val in test_cases:
        result = is_negative(val)
        print(f"is_negative({val}) = {result}")