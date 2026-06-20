def find_opposite_truth_value(value: bool) -> bool:
    return int(not value)

if __name__ == '__main__':
    print(find_opposite_truth_value(True))
    print(find_opposite_truth_value(False))