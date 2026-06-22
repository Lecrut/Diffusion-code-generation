def _validate_boolean(value):
    if type(value) is not bool:
        raise ValueError("Input must be a boolean value")

def invert_truth(value):
    _validate_boolean(value)
    return not value

if __name__ == '__main__':
    print(invert_truth(True))
    print(invert_truth(False))