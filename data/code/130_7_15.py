def check_zero(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Input must be an integer or float.")
    return value == 0

if __name__ == '__main__':
    sample_values = [5, 0, -3, 0, 10, "a", 4.5]
    for val in sample_values:
        try:
            result = check_zero(val)
            print(f"Input {val} is {'zero' if result else 'not zero'}.")
        except TypeError as e:
            print(e)