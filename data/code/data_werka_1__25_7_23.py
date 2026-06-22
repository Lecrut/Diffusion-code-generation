def is_zero_string(input_string):
    try:
        number = float(input_string)
        return number == 0
    except ValueError:
        return False

if __name__ == '__main__':
    test_values = ["0", "0.0", "-0", "1", "abc", "0x0"]
    for value in test_values:
        print(f"'{value}' is zero: {is_zero_string(value)}")