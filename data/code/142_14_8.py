def compare_truth_values(a: bool, b: bool) -> bool:
    return a == b
if __name__ == '__main__':
    print(compare_truth_values(True, True))
    print(compare_truth_values(False, False))
    print(compare_truth_values(True, False))