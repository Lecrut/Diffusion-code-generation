def is_odd(num):
    if not isinstance(num, (int, float)):
        raise TypeError("Input must be a numeric type.")
    try:
        num = int(float(num))
    except ValueError as ve:
        raise ValueError(f"Invalid number format: {ve}") from ve
    return num % 2 != 0
if __name__ == '__main__':
    test_cases = [5, -3.7, "10", None]
    for case in test_cases:
        try:
            result = is_odd(case)
            print(f"{case}: {result}")
        except Exception as e:
            print(f"Error with input '{case}': {e}")