def are_identical(arg1, arg2):
    return arg1 is arg2
if __name__ == '__main__':
    sample_value_1 = [1, 2, 3]
    sample_value_2 = sample_value_1
    sample_value_3 = [1, 2, 3]
    print(are_identical(sample_value_1, sample_value_2))
    print(are_identical(sample_value_1, sample_value_3))