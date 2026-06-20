def flags_to_booleans_and_evaluate_consistency(flag_list):
    boolean_map = {1: True, 0: False}
    booleans = [boolean_map[flag] for flag in flag_list]
    return all(booleans)

if __name__ == '__main__':
    sample_flags = [1, 0, 1, 1, 0]
    result = flags_to_booleans_and_evaluate_consistency(sample_flags)
    print(result)