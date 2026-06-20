def is_zero(value):
    if isinstance(value, (int, float)):
        return value == 0
    elif isinstance(value, str):
        try:
            num = float(value)
            return num == 0
        except ValueError:
            return False
    else:
        return False

if __name__ == '__main__':
    sample_values = [0, -1, 1.0, "0", "abc", None, [], {}, set()]
    for val in sample_values:
        print(f"{val} is zero: {is_zero(val)}")