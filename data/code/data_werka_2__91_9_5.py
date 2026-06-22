def _validate_boolean_input(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean type")
    return value

def negate_boolean(value):
    _validate_boolean_input(value)
    return not value

if __name__ == '__main__':
    print(negate_boolean(True))
    print(negate_boolean(False))