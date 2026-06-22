def find_opposite_truth(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean")
    is_true = value
    opposite = not is_true
    return opposite

if __name__ == '__main__':
    sample_input = True
    result = find_opposite_truth(sample_input)
    print(result)
    sample_input_2 = False
    result_2 = find_opposite_truth(sample_input_2)
    print(result_2)