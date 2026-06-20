def is_any_true(input_bool, bool_list):
    if not isinstance(bool_list, list) or not all(isinstance(item, bool) for item in bool_list):
        raise ValueError("bool_list must be a list of booleans")
    return input_bool or any(bool_list)

if __name__ == '__main__':
    print(is_any_true(True, [False, False]))
    print(is_any_true(False, [False, False]))
    print(is_any_true(False, [True, False]))
    print(is_any_true(True, [True, True]))
    print(is_any_true(False, []))