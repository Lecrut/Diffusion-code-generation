def assert_single_true(bools):
    return bool(sum(bools) == 1)

if __name__ == '__main__':
    sample_bools = [False, True, False]
    result = assert_single_true(sample_bools)
    print(result)