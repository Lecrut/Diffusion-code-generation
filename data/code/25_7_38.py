def is_zero(s):
    try:
        value = float(s)
        return value == 0
    except (ValueError, TypeError):
        return False

if __name__ == '__main__':
    test_values = ["0", "0.0", "-0", "1", "abc", None, "", "0x0"]
    for val in test_values:
        print(f"is_zero({val!r}): {is_zero(val)}")