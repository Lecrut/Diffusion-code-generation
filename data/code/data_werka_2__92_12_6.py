def find_opposite_truth_value(value: bool) -> bool:
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean")
    return bool(value ^ 1)

if __name__ == '__main__':
    print(find_opposite_truth_value(True))
    print(find_opposite_truth_value(False))