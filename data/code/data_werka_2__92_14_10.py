def _validate_boolean_input(value):
    if type(value) is not bool:
        raise ValueError("Input must be a boolean value")

def toggle_truth(value):
    _validate_boolean_input(value)
    return value ^ 1

if __name__ == '__main__':
    print(toggle_truth(True))
    print(toggle_truth(False))