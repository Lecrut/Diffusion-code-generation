def check_all_same_bools(values):
    if not values:
        return True
    first = values[0]
    for val in values[1:]:
        if val != first:
            return False
    return True

if __name__ == '__main__':
    sample_true = [True, True, True]
    sample_false = [False, False, False]
    sample_mixed = [True, False, True]
    
    result_true = check_all_same_bools(sample_true)
    result_false = check_all_same_bools(sample_false)
    result_mixed = check_all_same_bools(sample_mixed)
    
    print(result_true)
    print(result_false)
    print(result_mixed)