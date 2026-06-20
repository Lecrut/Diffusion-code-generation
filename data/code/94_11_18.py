def is_any_true(data, bool_list):
    if not isinstance(data, bool) or not all(isinstance(item, bool) for item in bool_list):
        raise ValueError("First argument must be a boolean and the second argument must be a list of booleans.")
    return data or any(bool_list)

if __name__ == '__main__':
    print(is_any_true(True, [False, False]))
    print(is_any_true(False, [True, False]))
    print(is_any_true(False, [False, True]))
    print(is_any_true(False, []))