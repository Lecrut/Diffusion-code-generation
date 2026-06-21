def find_opposite_truth_value(value: bool) -> bool:
    mask: int = 1
    inverted: int = value ^ mask
    result: bool = bool(inverted)
    return result

if __name__ == '__main__':
    sample_input: bool = False
    output: bool = find_opposite_truth_value(sample_input)
    print(output)
    sample_input_2: bool = True
    output_2: bool = find_opposite_truth_value(sample_input_2)
    print(output_2)