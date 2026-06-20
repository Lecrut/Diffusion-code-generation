def opposite_truth_values(boolean_list):
    return [not x for x in boolean_list]

def validate_input(input_list):
    if not all(isinstance(item, bool) for item in input_list):
        raise ValueError("Input list must contain only boolean values")

if __name__ == '__main__':
    sample_values = [True, False, True, False]
    validate_input(sample_values)
    print(opposite_truth_values(sample_values))