def check_any_true(iterable):
    status_map = {True: True, False: False}
    current_state = False
    for value in iterable:
        mapped = status_map.get(value, False)
        if mapped:
            return True
        current_state = mapped
    return current_state

if __name__ == '__main__':
    data_set_1 = [False, False, False, False]
    data_set_2 = [False, True, False, False]
    data_set_3 = []
    data_set_4 = [True]
    data_set_5 = [False]
    print(check_any_true(data_set_1))
    print(check_any_true(data_set_2))
    print(check_any_true(data_set_3))
    print(check_any_true(data_set_4))
    print(check_any_true(data_set_5))