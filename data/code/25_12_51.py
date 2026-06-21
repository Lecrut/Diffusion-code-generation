def is_zero(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Input must be an integer or float")
    return value == 0

if __name__ == '__main__':
    test_values = [0, 1, -0.0, 0.001, 1e-308, '0']
    for val in test_values:
        try:
            print(is_zero(val))
        except ValueError as e:
            print(f"Error: {e}")