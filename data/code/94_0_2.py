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
    print(f"Result for {sample_list_true}: {result1}")
    result2 = check_at_least_one_true(sample_list_false)
    print(f"Result for {sample_list_false}: {result2}")
    result3 = check_at_least_one_true(sample_list_all_true)
    print(f"Result for {sample_list_all_true}: {result3}")
    result4 = check_at_least_one_true(sample_list_empty)
    print(f"Result for {sample_list_empty}: {result4}")