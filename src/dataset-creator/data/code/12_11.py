def check_parity(value: int) -> bool:
    try:
        num = value
        return num % 2 == 0
    except Exception as e:
        raise TypeError(f"Input must be an integer, got {type(value).__name__}: {e}")
if __name__ == '__main__':
    test_cases = [10, -3, 42, 0]
    for case in test_cases:
        try:
            result = check_parity(case)
            print(f"Parity of {case} is {'even' if result else 'odd'}")
        except (TypeError, ValueError) as exc:
            print(f"Error processing {case}: {exc}")