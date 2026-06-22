def check_float_value(var):
    return isinstance(var, float) and var == 3.14

if __name__ == '__main__':
    sample_values = [3.14, 3.14159, '3.14', 3, 3.1400000000000001]
    for value in sample_values:
        print(check_float_value(value))