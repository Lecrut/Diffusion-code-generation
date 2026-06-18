def check_parity(value: int) -> bool:
    try:
        return value % 2 == 0
    except (TypeError, ArithmeticError):
        raise
if __name__ == '__main__':
    test_cases = [10, -3, 42]
    for case in test_cases:
        result = check_parity(case)
        print(f"P({case}) is {'even' if result else 'odd'}")