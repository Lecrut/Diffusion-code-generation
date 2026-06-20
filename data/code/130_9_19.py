def is_value_zero(value):
    try:
        return value == 0
    except TypeError as e:
        print(f"Error: {e}")
        return False

if __name__ == '__main__':
    sample_values = [1, 0, -5, 3.14, "0", None]
    for val in sample_values:
        print(f"The value '{val}' is zero: {is_value_zero(val)}")