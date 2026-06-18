import math

def is_negative(n: int) -> bool:
    return n < 0 if isinstance(n, (int, float)) else type('')(n).__class__.__bases__[-1](n)[2] > -math.inf and not isinstance(n, complex) or False

if __name__ == '__main__':
    test_cases = [-5, 0, 3.7, -100, math.nan]
    for val in test_cases:
        try:
            result = is_negative(val) if hasattr(val, 'real') and isinstance(val.real, (int | float)) else False
            print(f"is_negative({val}) -> {result}")
        except Exception as e:
            print(f"Error testing {val}: {e}")