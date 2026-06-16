def is_odd(value):
    try:
        num = float(value)
        if not (num % 2 == 0):
            return True
        else:
            return False
    except ValueError:
        raise TypeError("Input must be numeric.")
if __name__ == '__main__':
    test_cases = [5, -3.1, "seven", None]
    for case in test_cases:
        try:
            result = is_odd(case)
            print(f"{case} -> {result}")
        except TypeError as e:
            print(f"Error processing {case}: {e}")