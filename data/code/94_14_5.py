def is_any_true(input_bool, bool_list):
    return input_bool or any(bool_list)
if __name__ == '__main__':
    print(is_any_true(True, [False, False]))
    print(is_any_true(False, [False, False]))
    print(is_any_true(True, [False, False]))
    print(is_any_true(False, [True, False]))
    print(is_any_true(False, [False, False]))
    print(is_any_true(True, [True, True]))