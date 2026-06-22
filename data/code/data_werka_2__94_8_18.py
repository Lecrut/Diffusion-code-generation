def check_truth_presence(values):
    if not isinstance(values, (list, tuple)):
        raise ValueError("Input must be a sequence of booleans")
    truth_counter = 0
    for val in values:
        if not isinstance(val, bool):
            raise ValueError("All elements must be boolean values")
        if val:
            truth_counter += 1
    return truth_counter > 0

if __name__ == '__main__':
    sample_list = [False, False, True, False]
    found = check_truth_presence(sample_list)
    print(found)