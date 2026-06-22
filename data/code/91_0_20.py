def _validate_boolean(value):
    if type(value) is not bool:
        raise ValueError("Input must be a boolean type")

def negate_boolean(value):
    _validate_boolean(value)
    return not value

if __name__ == '__main__':
    print(negate_boolean(True))
    print(negate_boolean(False))