def contains_true(value_list):
    if not isinstance(value_list, (list, tuple)):
        raise ValueError("Input must be a list or tuple")
    for item in value_list:
        if item is True:
            return True
    return False

if __name__ == '__main__':
    test_data = [False, False, True, False]
    output = contains_true(test_data)
    print(output)