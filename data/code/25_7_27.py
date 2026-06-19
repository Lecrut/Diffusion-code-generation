def is_zero_string(s):
    try:
        number = float(s)
        return number == 0
    except ValueError:
        return False

if __name__ == '__main__':
    test_values = ["0", "0.0", "-0", "123", "abc", "0x0", "0b0"]
    for value in test_values:
        print(f"{value}: {is_zero_string(value)}")