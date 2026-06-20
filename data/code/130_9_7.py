def is_zero(value):
    try:
        return value == 0
    except TypeError:
        print(f"TypeError: Cannot determine if {value} is zero.")
        return False

if __name__ == '__main__':
    sample_values = [1, 0, -5.0, "0", None, True, [], {}, set()]
    for val in sample_values:
        result = is_zero(val)
        print(f"{val} is zero: {result}")