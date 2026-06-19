def is_zero_string(s):
    try:
        value = float(s)
        return value == 0
    except (ValueError, TypeError):
        return False

if __name__ == '__main__':
    test_values = ["0", "0.0", "-0", "1", "abc", None, ""]
    for value in test_values:
        print(is_zero_string(value))