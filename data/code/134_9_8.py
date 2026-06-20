def assert_single_true(boolean_list):
    return sum(boolean_list) == 1

if __name__ == '__main__':
    sample_values = [False, True, False]
    result = assert_single_true(sample_values)
    print(result)