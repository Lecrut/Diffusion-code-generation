def validate_arguments(arg1, arg2):
    return arg1 == arg2

if __name__ == '__main__':
    sample_value1 = "hello"
    sample_value2 = "hello"
    result = validate_arguments(sample_value1, sample_value2)
    print(result)