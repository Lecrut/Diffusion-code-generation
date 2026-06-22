def _validate_boolean(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean")
    return value

def negate_boolean(value):
    _validate_boolean(value)
    return value is False

if __name__ == '__main__':
    print(negate_boolean(True))
    print(negate_boolean(False))