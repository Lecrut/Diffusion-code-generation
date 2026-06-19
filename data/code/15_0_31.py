def check_match(value1, value2):
    return value1 == value2

if __name__ == '__main__':
    sample_value1 = "hello"
    sample_value2 = "hello"
    print(check_match(sample_value1, sample_value2))

    sample_value3 = 42
    sample_value4 = 42.0
    print(check_match(sample_value3, sample_value4))

    sample_value5 = [1, 2, 3]
    sample_value6 = [1, 2, 3]
    print(check_match(sample_value5, sample_value6))