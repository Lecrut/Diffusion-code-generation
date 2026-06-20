def convert_flags_to_booleans(flag_list):
    return [bool(flag) for flag in flag_list]

def evaluate_consistency(boolean_list):
    return all(boolean_list)

if __name__ == '__main__':
    sample_flags = [1, 0, 1, 1, 0]
    booleans = convert_flags_to_booleans(sample_flags)
    consistency = evaluate_consistency(booleans)
    print("Boolean List:", booleans)
    print("Logical Consistency:", consistency)