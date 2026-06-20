def assert_single_true(properties):
    if not isinstance(properties, list):
        raise ValueError("Input must be a list")
    
    true_count = sum(1 for p in properties if p)
    return true_count == 1

if __name__ == '__main__':
    sample_properties = [False, True, False]
    result = assert_single_true(sample_properties)
    print(result)