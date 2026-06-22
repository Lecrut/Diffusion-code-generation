def check_any_true(values):
    if not isinstance(values, (list, tuple)):
        raise TypeError("Input must be a list or tuple")
    if len(values) == 0:
        return False
    return any(values)

if __name__ == '__main__':
    test_list = [False, False, False]
    print(check_any_true(test_list))
    test_list_with_true = [False, True, False]
    print(check_any_true(test_list_with_true))
    empty_list = []
    print(check_any_true(empty_list))
    try:
        check_any_true("not a list")
    except TypeError as e:
        print("Caught expected error")