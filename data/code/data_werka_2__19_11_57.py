def check_float_and_value(variable):
    return isinstance(variable, float) and variable == 3.14

if __name__ == '__main__':
    sample_values = [3.14, 3.15, '3.14', 3, 3.1400000000000001]
    for value in sample_values:
        result = check_float_and_value(value)
        print(f"{value}: {result}")