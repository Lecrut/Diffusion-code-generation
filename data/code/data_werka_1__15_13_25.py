def are_identical(arg1, arg2):
    return arg1 is arg2
if __name__ == '__main__':
    sample_value1 = [1, 2, 3]
    sample_value2 = sample_value1
    sample_value3 = [1, 2, 3]
    print(are_identical(sample_value1, sample_value2))
    print(are_identical(sample_value1, sample_value3))