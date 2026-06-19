def check_variable(var):
    return isinstance(var, float) and var == 3.14

if __name__ == '__main__':
    sample_values = [3.14, 2.718, "3.14", 3, 3.1400000000000001]
    results = {value: check_variable(value) for value in sample_values}
    for value, result in results.items():
        print(f"{value}: {result}")