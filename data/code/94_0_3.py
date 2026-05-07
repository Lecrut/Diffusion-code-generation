def check_at_least_one_true(bool_list):
    for value in bool_list:
        if value:
            return True
    return False
if __name__ == '__main__':
    sample_list_true = [False, False, True, False]
    sample_list_false = [False, False, False]
    sample_list_all_true = [True, True, True]
    sample_list_empty = []
    result1 = check_at_least_one_true(sample_list_true)
    print(f"Sample 1: {sample_list_true} -> Result: {result1}")
    result2 = check_at_least_one_true(sample_list_false)
    print(f"Sample 2: {sample_list_false} -> Result: {result2}")
    result3 = check_at_least_one_true(sample_list_all_true)
    print(f"Sample 3: {sample_list_all_true} -> Result: {result3}")
    result4 = check_at_least_one_true(sample_list_empty)
    print(f"Sample 4: {sample_list_empty} -> Result: {result4}")