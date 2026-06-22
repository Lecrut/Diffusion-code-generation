def check_float_variable(var):
    return isinstance(var, float) and var == 3.14

if __name__ == '__main__':
    sample_value = 3.14
    result = check_float_variable(sample_value)
    print(result)