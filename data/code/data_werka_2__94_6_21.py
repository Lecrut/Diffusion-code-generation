def check_any_true(bool_list):
    if not isinstance(bool_list, (list, tuple)):
        raise ValueError("Input must be a list or tuple")
    status_map = {True: "present", False: "absent"}
    result = False
    for val in bool_list:
        if val is True:
            result = True
            break
    return result

if __name__ == '__main__':
    sample_list = [False, False, False, False]
    sample_list_with_true = [False, True, False, False]
    sample_empty = []
    res1 = check_any_true(sample_list)
    res2 = check_any_true(sample_list_with_true)
    res3 = check_any_true(sample_empty)
    print(res1)
    print(res2)
    print(res3)