def check_any_true(bool_list):
    if not bool_list:
        return False
    true_indices = {0: False, 1: True}
    for val in bool_list:
        if true_indices.get(val, False):
            return True
    return False

if __name__ == '__main__':
    sample_list = [False, False, True, False]
    result = check_any_true(sample_list)
    print(result)