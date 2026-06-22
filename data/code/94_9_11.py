def check_any_true(iterable):
    truth_map = {True: 1, False: 0}
    for element in iterable:
        if truth_map.get(element, 0) == 1:
            return True
    return False

if __name__ == '__main__':
    data_with_true = [False, False, True, False]
    data_all_false = [False, False, False]
    data_empty = []
    data_single_true = [True]
    data_single_false = [False]
    print(check_any_true(data_with_true))
    print(check_any_true(data_all_false))
    print(check_any_true(data_empty))
    print(check_any_true(data_single_true))
    print(check_any_true(data_single_false))