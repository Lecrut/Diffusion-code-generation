def opposite_truth_values(boolean_list):
    if not all(isinstance(x, bool) for x in boolean_list):
        raise ValueError("Input must be a list of boolean values")
    return [not x for x in boolean_list]

if __name__ == '__main__':
    sample_values = [True, False, True, False]
    print(opposite_truth_values(sample_values))