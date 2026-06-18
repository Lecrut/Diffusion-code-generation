def is_odd(value):
    try:
        num = float(value)
        if not isinstance(num, (int, float)):
            raise TypeError("Input must be numeric.")
        return int(num) % 2 != 0
    except ValueError as e:
        raise ValueError(f"Invalid input type or value: {e}")
if __name__ == '__main__':
    test_cases = [5, "7", -3.1, True, None]
    for case in test_cases:
        try:
            result = is_odd(case)
            print(f"is_odd({case}) -> {result}")
        except Exception as ex:
            print(f"Error processing {case}: {ex}")