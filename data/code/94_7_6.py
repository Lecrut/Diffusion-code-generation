def check_any_true(boolean_list):
    return any(boolean_list)

if __name__ == '__main__':
    sample_lists = {
        "list1": [False, False, False, True, False],
        "list2": [False, False, False],
        "list3": [True, True, True],
        "list4": [],
        "list5": [False]
    }

    for name, lst in sample_lists.items():
        print(f"{name}: {check_any_true(lst)}")