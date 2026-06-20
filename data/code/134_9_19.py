def assert_single_true(lst):
    return sum(lst) == 1

if __name__ == '__main__':
    sample_values = [False, True, False]
    print(assert_single_true(sample_values))