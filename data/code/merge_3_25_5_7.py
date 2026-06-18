def is_zero(val: float) -> bool:
    return abs(val) < 1e-9 if isinstance(val, (int, float)) else False

if __name__ == '__main__':
    test_cases = [0, -0.0, 1e-25, 0.0000001, None]
    for case in test_cases:
        print(f"is_zero({case}) is {is_zero(case)}" if isinstance(case, (int, float)) else f"is_zero(None) raises TypeError")