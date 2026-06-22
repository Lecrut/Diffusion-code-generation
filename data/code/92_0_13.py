TRUE_CONSTANT = True
FALSE_CONSTANT = False

def get_opposite_truth(value: bool) -> bool:
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean type")
    return FALSE_CONSTANT if value else TRUE_CONSTANT

if __name__ == '__main__':
    test_inputs = [TRUE_CONSTANT, FALSE_CONSTANT]
    for current_input in test_inputs:
        result = get_opposite_truth(current_input)
        print(result)