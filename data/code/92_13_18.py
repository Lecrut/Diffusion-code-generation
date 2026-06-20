def validate_input(value: bool) -> None:
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean value.")

def find_opposite_truth_value(value: bool) -> bool:
    validate_input(value)
    return int(not value)

if __name__ == '__main__':
    print(find_opposite_truth_value(True))
    print(find_opposite_truth_value(False))