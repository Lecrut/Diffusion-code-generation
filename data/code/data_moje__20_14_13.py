def is_even(value):
    if not isinstance(value, int) or isinstance(value, bool):
        return "InvalidInput"
    return value % 2 == 0

if __name__ == '__main__':
    test_values = [2, 3, 0, -1, 4.5, "string", None, True]
    for val in test_values:
        print(is_even(val))