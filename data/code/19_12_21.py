def is_float_and_equals_3_14(variable):
    return isinstance(variable, float) and variable == 3.14

if __name__ == '__main__':
    sample_value = 3.14
    result = is_float_and_equals_3_14(sample_value)
    print(result)