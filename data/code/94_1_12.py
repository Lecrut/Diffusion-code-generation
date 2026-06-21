def check_any_true(iterable):
    truth_counter = 0
    for value in iterable:
        if value:
            truth_counter += 1
            break
    return truth_counter > 0

if __name__ == '__main__':
    data_set_a = [False, False, False]
    data_set_b = [False, True, False]
    data_set_c = []
    data_set_d = [False]

    result_a = check_any_true(data_set_a)
    result_b = check_any_true(data_set_b)
    result_c = check_any_true(data_set_c)
    result_d = check_any_true(data_set_d)

    print(result_a)
    print(result_b)
    print(result_c)
    print(result_d)