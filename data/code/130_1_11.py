def is_integer_zero(number):
    if not isinstance(number, int):
        raise ValueError("Input must be an integer.")
    return number == 0

if __name__ == '__main__':
    sample_values = [0, 5, -3, 0]
    for value in sample_values:
        try:
            result = is_integer_zero(value)
            print(f"Checking value: {value}, Is zero: {result}")
        except ValueError as e:
            print(e)