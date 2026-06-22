def check_any_true(iterable):
    results = {True: True, False: False}
    for element in iterable:
        if results.get(element, False):
            return True
    return False

if __name__ == '__main__':
    sample_list = [False, False, False, False]
    sample_list_with_true = [False, True, False, False]
    empty_list = []
    single_true = [True]
    single_false = [False]
    print(check_any_true(sample_list))
    print(check_any_true(sample_list_with_true))
    print(check_any_true(empty_list))
    print(check_any_true(single_true))
    print(check_any_true(single_false))