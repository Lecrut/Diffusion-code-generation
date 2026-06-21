def _validate_boolean(value):
    if type(value) is not bool:
        raise ValueError("Input must be a boolean")

def invert_boolean(value):
    _validate_boolean(value)
    return value ^ True

if __name__ == '__main__':
    print(invert_boolean(True))
    print(invert_boolean(False))
    print(invert_boolean(True) == False)
    print(invert_boolean(False) == True)