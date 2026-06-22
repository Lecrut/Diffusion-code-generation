BOOL_XOR_CONSTANT: int = 1

def find_opposite_truth_value(value: bool) -> bool:
    return bool(value ^ BOOL_XOR_CONSTANT)

if __name__ == '__main__':
    true_result = find_opposite_truth_value(True)
    false_result = find_opposite_truth_value(False)
    print(true_result)
    print(false_result)