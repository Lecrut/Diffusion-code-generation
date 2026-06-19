def are_identical(arg1, arg2):
    return arg1 is arg2
if __name__ == '__main__':
    sample_value1 = 'hello'
    sample_value2 = 'hello'
    sample_value3 = 'world'
    print(are_identical(sample_value1, sample_value2))
    print(are_identical(sample_value1, sample_value3))