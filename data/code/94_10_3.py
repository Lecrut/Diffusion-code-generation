import operator
def check_any_true(bool_list):
    if not bool_list:
        return False
    return any(bool_list)
if __name__ == '__main__':
    sample_list_true = [False, False, True, False]
    sample_list_all_false = [False, False, False]
    sample_list_empty = []
    sample_list_all_true = [True, True, True]
    print(f"Sample 1: {sample_list_true} -> Result: {check_any_true(sample_list_true)}")
    print(f"Sample 2: {sample_list_all_false} -> Result: {check_any_true(sample_list_all_false)}")
    print(f"Sample 3: {sample_list_empty} -> Result: {check_any_true(sample_list_empty)}")
    print(f"Sample 4: {sample_list_all_true} -> Result: {check_any_true(sample_list_all_true)}")