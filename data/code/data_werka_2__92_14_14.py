def _validate_boolean(input_value):
    if type(input_value) is not bool:
        raise ValueError("Expected a boolean type")
    return input_value

def invert_truth(input_value):
    is_valid = _validate_boolean(input_value)
    return not is_valid

if __name__ == '__main__':
    print(invert_truth(True))
    print(invert_truth(False))