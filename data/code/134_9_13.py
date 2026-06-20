def assert_single_true(lst):
    return lst.count(True) == 1

if __name__ == '__main__':
    sample_values = [False, True, False]
    result = assert_single_true(sample_values)
    print(result)