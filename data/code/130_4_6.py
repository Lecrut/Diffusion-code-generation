def is_zero(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Input must be an integer or float")
    return value == 0

if __name__ == '__main__':
    test_values = [0, 1, -2, 3.14, 0j]
    for val in test_values:
        try:
            result = is_zero(val)
            print(f"is_zero({val}) = {result}")
        except ValueError as e:
            print(e)