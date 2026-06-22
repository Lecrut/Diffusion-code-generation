def check_any_true(iterable):
    true_count = 0
    false_count = 0
    total_count = 0
    for value in iterable:
        total_count += 1
        if value:
            true_count += 1
        else:
            false_count += 1
    if true_count > 0:
        return True
    return False

if __name__ == '__main__':
    test_data_1 = [False, False, True, False]
    test_data_2 = [False, False, False]
    test_data_3 = []
    test_data_4 = [True]
    test_data_5 = [False, True, False]
    print(check_any_true(test_data_1))
    print(check_any_true(test_data_2))
    print(check_any_true(test_data_3))
    print(check_any_true(test_data_4))
    print(check_any_true(test_data_5))