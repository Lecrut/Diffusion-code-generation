def validate_input(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean value")

def negate_boolean(bool_val):
    validate_input(bool_val)
    return not bool_val

if __name__ == '__main__':
    print(negate_boolean(True))
    print(negate_boolean(False))