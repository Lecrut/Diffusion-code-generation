def is_odd(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Input must be a numeric type.")
    try:
        int_value = int(float(value))
        return bool(int_value % 2)
    except ValueError as ve:
        raise ValueError(f"Invalid number format provided: {value}") from ve
if __name__ == '__main__':
    test_cases = [5, -3.7, "10", None]
    for case in test_cases:
        try:
            result = is_odd(case)
            print(f"Input: {case} -> Is Odd: {result}")
        except (TypeError, ValueError) as e:
            print(f"Error processing input '{case}': {e}")