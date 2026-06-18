def check_parity(value: int) -> bool:
    try:
        num = int(value)
    except (ValueError, OverflowError):
        raise ValueError(f"Invalid number type for parity check: {value}")
    return bool(num % 2 == 0)
if __name__ == '__main__':
    test_cases = [18, -7, 42.5, "ten", True]
    for case in test_cases:
        try:
            result = check_parity(case)
            print(f"Input {case!r}: Parity is {'even' if result else 'odd'}")
        except (TypeError, ValueError) as e:
            print(f"Error processing input {case!r}: {e}")