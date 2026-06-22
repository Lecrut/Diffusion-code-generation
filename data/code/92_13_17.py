def _validate_boolean(value):
    if type(value) is not bool:
        raise ValueError("Input must be a boolean type")
    return value

def invert_boolean(value):
    _validate_boolean(value)
    return value ^ True

if __name__ == '__main__':
    print(invert_boolean(True))
    print(invert_boolean(False))
    print(invert_boolean(True) is False)
    print(invert_boolean(False) is True)