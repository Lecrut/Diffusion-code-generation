def find_opposite_truth(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean")
    is_truth = value
    opposite_is_truth = not is_truth
    return opposite_is_truth

if __name__ == '__main__':
    sample_input_1 = False
    sample_input_2 = True
    output_1 = find_opposite_truth(sample_input_1)
    output_2 = find_opposite_truth(sample_input_2)
    print(output_1)
    print(output_2)