def validate_input(val):
    if not isinstance(val, bool):
        raise ValueError("Input must be a boolean")

def are_both_true(val1, val2):
    validate_input(val1)
    validate_input(val2)
    return val1 and val2

if __name__ == '__main__':
    print(are_both_true(True, True))
    print(are_both_true(False, True))
    print(are_both_true(True, False))
    print(are_both_true(False, False))