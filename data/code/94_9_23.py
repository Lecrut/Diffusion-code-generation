def check_any_true(iterable):
    if not iterable:
        return False
    for element in iterable:
        if element is True or element is False:
            if element:
                return True
        elif element:
            return True
    return False

if __name__ == '__main__':
    sample_list_1 = [False, False, True, False]
    sample_list_2 = [False, False, False]
    sample_list_3 = []
    sample_list_4 = [True]
    sample_list_5 = [0, 1, 2]
    sample_list_6 = [None, False, 0]
    print(check_any_true(sample_list_1))
    print(check_any_true(sample_list_2))
    print(check_any_true(sample_list_3))
    print(check_any_true(sample_list_4))
    print(check_any_true(sample_list_5))
    print(check_any_true(sample_list_6))