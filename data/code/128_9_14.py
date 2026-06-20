def is_negative(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Input must be an integer or float")
    return value < 0

if __name__ == '__main__':
    test_values = [-10, 5, 0, -3.14, 2]
    for val in test_values:
        try:
            print(f"Value {val} is negative: {is_negative(val)}")
        except ValueError as e:
            print(e)