def convert_and_evaluate_flags(flag_list):
    bool_list = [bool(flag) for flag in flag_list]
    return all(bool_list)

if __name__ == '__main__':
    sample_flags = [1, 0, 1, 1]
    result = convert_and_evaluate_flags(sample_flags)
    print(result)