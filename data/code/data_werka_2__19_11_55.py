def validate_float(value):
    if not isinstance(value, float):
        raise ValueError("Input must be of type float")
    return value == 3.14

if __name__ == '__main__':
    try:
        sample_values = [3.14, 3.14159, '3.14', 3, 3.1400000000000001]
        for value in sample_values:
            result = validate_float(value)
            print(f"{value}: {result}")
    except ValueError as e:
        print(e)