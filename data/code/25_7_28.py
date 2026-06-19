def is_zero(value):
    try:
        number = float(value)
        return number == 0
    except (ValueError, TypeError):
        return False

if __name__ == '__main__':
    test_values = ["0", "0.0", "-0", "abc", None, "", "123"]
    for value in test_values:
        print(f"is_zero({value!r}): {is_zero(value)}")