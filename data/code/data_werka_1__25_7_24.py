def is_zero_string(value):
    try:
        number = float(value)
        return number == 0
    except (ValueError, TypeError):
        return False

if __name__ == '__main__':
    test_values = ['0', '0.0', '-0', '+0', '0e0', 'abc', None, '', ' ', '0.0001']
    for val in test_values:
        print(f"is_zero_string({val!r}): {is_zero_string(val)}")