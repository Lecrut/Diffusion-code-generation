def find_opposite_truth_value(value: bool) -> bool:
    return value ^ True

if __name__ == '__main__':
    result1 = find_opposite_truth_value(True)
    print(result1)
    result2 = find_opposite_truth_value(False)
    print(result2)