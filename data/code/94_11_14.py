def check_any_true(values):
    if not isinstance(values, (list, tuple)):
        raise ValueError("Input must be a sequence")
    if len(values) == 0:
        return False
    for item in values:
        if item is True:
            return True
    return False

if __name__ == '__main__':
    test_list = [False, False, False]
    test_any = check_any_true(test_list)
    print(test_any)
    test_any_mixed = check_any_true([False, True, False])
    print(test_any_mixed)