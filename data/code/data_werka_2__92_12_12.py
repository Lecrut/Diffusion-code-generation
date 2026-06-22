def _validate_boolean_input(value):
    if type(value) is not bool:
        raise ValueError("Input must be a boolean")
    return value

def find_opposite_truth_value(value: bool) -> bool:
    _validate_boolean_input(value)
    return value ^ 1

if __name__ == '__main__':
    result_true = find_opposite_truth_value(True)
    result_false = find_opposite_truth_value(False)
    print(result_true)
    print(result_false)