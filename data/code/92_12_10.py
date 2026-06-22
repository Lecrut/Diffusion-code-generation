def find_opposite_truth_value(value: bool) -> bool:
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean")
    return value ^ 1

if __name__ == '__main__':
    sample_true: bool = True
    sample_false: bool = False
    result_true: bool = find_opposite_truth_value(sample_true)
    result_false: bool = find_opposite_truth_value(sample_false)
    print(result_true)
    print(result_false)