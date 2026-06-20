TRUE_FLAG = 1
FALSE_FLAG = 0

def flags_to_booleans_and_evaluate_consistency(flag_list):
    booleans = [bool(flag) for flag in flag_list]
    return all(booleans)

if __name__ == '__main__':
    sample_flags = [TRUE_FLAG, FALSE_FLAG, TRUE_FLAG, TRUE_FLAG, FALSE_FLAG]
    result = flags_to_booleans_and_evaluate_consistency(sample_flags)
    print(result)