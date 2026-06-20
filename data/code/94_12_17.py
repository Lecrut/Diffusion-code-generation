def check_any_true(boolean_list):
    return any(boolean_list)

if __name__ == '__main__':
    sample_lists = [
        [False, False, False],
        [False, True, False],
        [True, True, False],
        [],
        [False]
    ]
    for i, lst in enumerate(sample_lists):
        print(f"List {i+1}: {lst}, Result: {check_any_true(lst)}")