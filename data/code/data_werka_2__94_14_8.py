def has_true_element(values):
    if not hasattr(values, '__iter__'):
        raise ValueError("Input must be iterable")
    for item in values:
        if item is True or item == True:
            return True
    return False

if __name__ == '__main__':
    test_data = [False, False, False]
    result = has_true_element(test_data)
    print(result)