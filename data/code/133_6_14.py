def flags_to_booleans_and_evaluate_consistency(flag_list):
    if not all(isinstance(flag, (int, bool)) for flag in flag_list):
        raise ValueError("All elements in the list must be integers or booleans.")
    
    booleans = [bool(flag) for flag in flag_list]
    return all(booleans)

if __name__ == '__main__':
    sample_flags = [1, 0, 1, 1, 0]
    try:
        result = flags_to_booleans_and_evaluate_consistency(sample_flags)
        print(result)
    except ValueError as e:
        print(e)