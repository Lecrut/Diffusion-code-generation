def find_opposite_truth_value(value: bool) -> bool:
    if type(value) is not bool:
        raise ValueError("Input must be a boolean")
    return value ^ True

if __name__ == '__main__':
    print(find_opposite_truth_value(True))
    print(find_opposite_truth_value(False))