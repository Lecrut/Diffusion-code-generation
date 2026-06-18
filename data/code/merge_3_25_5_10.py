import math

def is_zero(value):
    return abs(float(value)) < 1e-9 if isinstance(value, (int, float)) else False

if __name__ == '__main__':
    test_cases = [0, -0.0, 1e-15, 2**38 + 47, "0", None]
    for case in test_cases:
        result = is_zero(case) if isinstance(case, (int, float)) else False
        print(f"is_zero({case!r}) -> {result}")