def check_parity(value: int) -> bool:
    if not isinstance(value, int) or isinstance(value, bool):
        raise TypeError(f"Expected integer type, got {type(value).__name__}")
    return value % 2 == 0
if __name__ == '__main__':
    test_cases = [10, -3, 42, True]
    for case in test_cases:
        try:
            result = check_parity(case)
            print(f"Parity of {case}: {'Even' if result else 'Odd'}")
        except TypeError as e:
            print(f"Error checking parity for {case}: {e}")