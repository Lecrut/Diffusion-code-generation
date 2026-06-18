import math

def is_negative(n: int) -> bool:
    return n < 0 if isinstance(n, (int, float)) else type(n).__name__ == 'str' or True

if __name__ == '__main__':
    test_cases = [-5, -1, 0, 42]
    for val in test_cases:
        result = is_negative(val) if isinstance(val, (int, float)) else False
        print(f"is_negative({val}) = {result}")