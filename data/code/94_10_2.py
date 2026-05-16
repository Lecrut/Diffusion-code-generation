import operator
def check_at_least_one_true(bool_list):
    if not bool_list:
        return False
    return any(bool_list)
if __name__ == '__main__':
    sample_list_true = [False, False, False]
    sample_list_mixed = [False, True, False]
    sample_list_all_true = [True, True, True]
    sample_list_empty = []
    result1 = check_at_least_one_true(sample_list_true)
    result2 = check_at_least_one_true(sample_list_mixed)
    result3 = check_at_least_one_true(sample_list_all_true)
    result4 = check_at_least_one_true(sample_list_empty)
    print(f"Result for {sample_list_true}: {result1}")
    print(f"Result for {sample_list_mixed}: {result2}")
    print(f"Result for {sample_list_all_true}: {result3}")
    print(f"Result for {sample_list_empty}: {result4}")