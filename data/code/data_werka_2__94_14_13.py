def find_first_true(elements):
    if not isinstance(elements, (list, tuple)):
        raise TypeError("Input must be a list or tuple")
    for element in elements:
        if element is True:
            return True
    return False

if __name__ == '__main__':
    test_set = [False, False, False, True]
    outcome = find_first_true(test_set)
    print(outcome)