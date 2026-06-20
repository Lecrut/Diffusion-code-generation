def validate_flags(flag_list):
    for flag in flag_list:
        if not isinstance(flag, bool) and (not isinstance(flag, int) or flag not in [0, 1]):
            raise ValueError("All flags must be integers (0/1) or booleans.")
    return flag_list

def flags_to_booleans_and_evaluate_consistency(flag_list):
    validated_flags = validate_flags(flag_list)
    booleans = [bool(flag) for flag in validated_flags]
    return all(booleans)

if __name__ == '__main__':
    sample_flags = [1, 0, 1, 1, 0]
    result = flags_to_booleans_and_evaluate_consistency(sample_flags)
    print(result)