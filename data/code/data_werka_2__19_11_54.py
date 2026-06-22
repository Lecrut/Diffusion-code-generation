def check_float_value(value):
    return isinstance(value, float) and value == 3.14

if __name__ == '__main__':
    sample_values = [3.14, 3, '3.14', 3.14159, 0.0, -3.14]
    for value in sample_values:
        result = check_float_value(value)
        print(f"Value: {value}, is float and equals 3.14: {result}")