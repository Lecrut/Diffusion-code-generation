def find_opposite_truth_value(value: bool) -> bool:
    return not value

if __name__ == '__main__':
    result_true = find_opposite_truth_value(False)
    result_false = find_opposite_truth_value(True)
    print(result_true, result_false)