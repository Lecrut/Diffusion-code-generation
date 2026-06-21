def is_zero_string(s):
    try:
        numeric_value = float(s)
        zero_check = (numeric_value == 0)
        return zero_check
    except ValueError:
        return False

if __name__ == '__main__':
    sample_values = ["0", "0.0", "-0", "123", "abc", "0x0", "0b1"]
    for value in sample_values:
        result = is_zero_string(value)
        print(f"is_zero_string('{value}'): {result}")