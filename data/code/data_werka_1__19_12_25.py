def check_float_value(var):
    return isinstance(var, float) and var == 3.14

if __name__ == '__main__':
    sample_values = [3.14, 3, '3.14', 3.140001, 3.139999]
    results = {value: check_float_value(value) for value in sample_values}
    for value, result in results.items():
        print(f"{value}: {result}")