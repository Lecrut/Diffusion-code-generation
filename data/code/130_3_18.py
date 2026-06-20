def is_zero(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Input must be an integer or float")
    return value == 0

if __name__ == '__main__':
    sample_values = [0, 5, -3, 0.0, "0", None]
    for value in sample_values:
        try:
            result = is_zero(value)
            print(f"Value: {value}, Is Zero: {result}")
        except ValueError as e:
            print(e)