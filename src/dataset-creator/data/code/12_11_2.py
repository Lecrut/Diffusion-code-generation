def check_parity(value: int) -> bool:
    try:
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"Expected 'int', got '{type(value).__name__}'.")
        return value % 2 == 0
    except Exception as e:
        raise ValueError(f"Invalid input provided: {e}")
if __name__ == '__main__':
    test_cases = [1, -5, 42, 0, True]
    for case in test_cases:
        try:
            result = check_parity(case)
            print(f"P({case}) -> {'Even' if result else 'Odd'}")
        except (TypeError, ValueError) as error:
            print(f"Error processing {case}: {error}")