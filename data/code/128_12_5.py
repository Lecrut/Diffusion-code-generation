def is_number(value):
    return isinstance(value, (int, float))

def is_negative(value):
    if not is_number(value):
        raise ValueError("Input must be a number")
    return value < 0

if __name__ == '__main__':
    sample_values = [10, -5, 0, -100, 3.14]
    for value in sample_values:
        try:
            result = is_negative(value)
            print(f"Value: {value}, Is Negative: {result}")
        except ValueError as e:
            print(e)