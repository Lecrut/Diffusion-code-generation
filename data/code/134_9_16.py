def assert_single_true(properties):
    if not isinstance(properties, list) or not all((isinstance(prop, bool) for prop in properties)):
        raise ValueError('Input must be a list of boolean values')
    true_count = sum(properties)
    return true_count == 1
if __name__ == '__main__':
    sample_properties = [False, True, False]
    result = assert_single_true(sample_properties)
    print(result)