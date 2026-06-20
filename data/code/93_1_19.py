def validate_inputs(a, b):
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Both inputs must be boolean values")

def are_both_false(a, b):
    validate_inputs(a, b)
    return not a and not b

if __name__ == '__main__':
    print(are_both_false(False, False))
    print(are_both_false(True, False))
    print(are_both_false(False, True))
    print(are_both_false(True, True))