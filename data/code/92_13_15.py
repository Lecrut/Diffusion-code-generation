def is_valid_input(value: bool) -> bool:
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean value.")
    return True

def find_opposite_truth_value(value: bool) -> bool:
    is_valid_input(value)
    return int(not value)

if __name__ == '__main__':
    print(find_opposite_truth_value(True))
    print(find_opposite_truth_value(False))