def is_zero_number(value):
    try:
        number = float(value)
        return number == 0
    except (ValueError, TypeError):
        return False

if __name__ == '__main__':
    test_values = ["0", "0.0", "-0", "1", "abc", None, True, False]
    for value in test_values:
        print(f"is_zero_number({value!r}): {is_zero_number(value)}")