def is_zero(number):
    if not isinstance(number, (int, float)):
        raise ValueError("Input must be a numeric value")
    return number == 0

if __name__ == '__main__':
    sample_values = [1, 2.5, 0, -3, 0.0, "zero"]
    for value in sample_values:
        try:
            result = is_zero(value)
            print(f"Value: {value}, Is Zero: {result}")
        except ValueError as e:
            print(e)