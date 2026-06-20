def assert_single_true(properties):
    return sum(properties) == 1

if __name__ == '__main__':
    sample_properties = [False, False, True, False]
    result = assert_single_true(sample_properties)
    print(result)