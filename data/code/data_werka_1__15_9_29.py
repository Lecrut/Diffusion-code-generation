def check_match(value1, value2):
    return value1 == value2
if __name__ == '__main__':
    sample_value1 = 42
    sample_value2 = 42
    result = check_match(sample_value1, sample_value2)
    print(result)
    sample_value3 = 'hello'
    sample_value4 = 'world'
    result = check_match(sample_value3, sample_value4)
    print(result)