def validate_exact_match(arg1, arg2):
    return arg1 == arg2

if __name__ == '__main__':
    sample_value1 = "hello"
    sample_value2 = "hello"
    result = validate_exact_match(sample_value1, sample_value2)
    print(result)