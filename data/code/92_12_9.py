def find_opposite_truth_value(value: bool) -> bool:
    mapping = {True: False, False: True}
    return mapping[value]

if __name__ == '__main__':
    print(find_opposite_truth_value(True))
    print(find_opposite_truth_value(False))