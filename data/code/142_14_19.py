def check_same_truth_value(a: bool, b: bool) -> bool:
    return a == b
if __name__ == '__main__':
    print(check_same_truth_value(True, True))
    print(check_same_truth_value(False, False))
    print(check_same_truth_value(True, False))