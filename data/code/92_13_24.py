def find_opposite_truth_value(value: bool) -> bool:
    return value ^ 1
if __name__ == '__main__':
    sample_value_1 = True
    sample_value_2 = False
    print(find_opposite_truth_value(sample_value_1))
    print(find_opposite_truth_value(sample_value_2))