def check_any_true(boolean_list):
    return any(boolean_list)

if __name__ == '__main__':
    sample_lists = [
        [False, False, False, True, False],
        [False, False, False],
        [True, True, True],
        [],
        [False]
    ]
    for lst in sample_lists:
        print(f"List: {lst}, Result: {check_any_true(lst)}")