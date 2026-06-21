TRUE_BIT: int = 1
FALSE_BIT: int = 0

def find_opposite_truth_value(value: bool) -> bool:
    return bool(value ^ TRUE_BIT)

if __name__ == '__main__':
    result_true: bool = find_opposite_truth_value(True)
    result_false: bool = find_opposite_truth_value(False)
    print(result_true)
    print(result_false)