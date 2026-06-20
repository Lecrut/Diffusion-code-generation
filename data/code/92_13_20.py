def find_opposite_truth_value(value: bool) -> bool:
    return not value
if __name__ == '__main__':
    sample1 = True
    sample2 = False
    print(find_opposite_truth_value(sample1))
    print(find_opposite_truth_value(sample2))