def find_opposite_truth_value(value: bool) -> bool:
    opposite_values = {True: False, False: True}
    return opposite_values[value]

if __name__ == '__main__':
    print(find_opposite_truth_value(True))
    print(find_opposite_truth_value(False))