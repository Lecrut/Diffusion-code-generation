def find_opposite_truth_value(value: bool) -> bool:
    truth_map = {True: False, False: True}
    return truth_map[value]

if __name__ == '__main__':
    print(find_opposite_truth_value(True))
    print(find_opposite_truth_value(False))