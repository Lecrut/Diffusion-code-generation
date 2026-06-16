def is_odd(num):
    if not isinstance(num, (int, float)):
        raise TypeError("Input must be a numeric type.")
    return num % 2 != 0 and isinstance(num, int)
if __name__ == '__main__':
    test_cases = [5.7, -3, "10", None]
    for value in test_cases:
        try:
            result = is_odd(value)
            print(f"{value}: {result}")
        except TypeError as e:
            print(f"Error processing {value}: {e}")