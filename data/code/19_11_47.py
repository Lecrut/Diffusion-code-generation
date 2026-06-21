def check_variable(value):
    return isinstance(value, float) and value == 3.14

if __name__ == '__main__':
    sample_value = 3.14
    result = check_variable(sample_value)
    print(result)