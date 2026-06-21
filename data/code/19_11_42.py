def check_float_value(value):
    return isinstance(value, float) and value == 3.14

if __name__ == '__main__':
    sample_values = [3.14, 3.14159, '3.14', 3, 3.0]
    for value in sample_values:
        print(check_float_value(value))