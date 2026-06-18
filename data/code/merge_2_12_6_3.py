def is_odd(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Input must be a numeric type.")
    try:
        int_value = int(float(value))
        return bool(int_value % 2)
    except ValueError as e:
        raise ValueError(f"Invalid number format: {e}")
if __name__ == '__main__':
    test_cases = [5, -3.7, "10", None]
    for case in test_cases:
        try:
            result = is_odd(case)
            print(f"{case} -> Odd: {result}")
        except (TypeError, ValueError) as error:
            print(f"Error processing {case}: {error}")