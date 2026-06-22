def check_all_same_bools(bool_list):
    if not bool_list:
        return True
    first = bool_list[0]
    for val in bool_list[1:]:
        if val != first:
            return False
    return True

if __name__ == '__main__':
    sample_true = [True, True, True]
    sample_false = [False, False, False]
    sample_mixed = [True, False, True]
    
    print(check_all_same_bools(sample_true))
    print(check_all_same_bools(sample_false))
    print(check_all_same_bools(sample_mixed))