def is_any_true(data, bool_list):
    return data or any(bool_list)

if __name__ == '__main__':
    print(is_any_true(True, [False, False]))
    print(is_any_true(False, [True, False]))
    print(is_any_true(False, [False, True]))
    print(is_any_true(False, []))