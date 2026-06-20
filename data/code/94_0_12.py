def check_at_least_one_true(bool_list):
    return any(bool_list)

if __name__ == '__main__':
    sample_lists = {
        "sample_list_true": [False, False, True, False],
        "sample_list_false": [False, False, False],
        "sample_list_all_true": [True, True, True],
        "sample_list_empty": []
    }
    
    for name, lst in sample_lists.items():
        result = check_at_least_one_true(lst)
        print(f"{name}: {lst} -> Result: {result}")