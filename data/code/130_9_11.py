def is_zero(value):
    try:
        return value == 0
    except TypeError as e:
        print(f"Type error: {e}")
        return False

if __name__ == '__main__':
    sample_values = [1, 0, -5, "0", None, {}, [], (), 3.14]
    for val in sample_values:
        print(f"The value {val} is zero: {is_zero(val)}")