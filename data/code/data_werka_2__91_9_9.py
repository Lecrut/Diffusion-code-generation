def validate_boolean(value):
    if type(value) is not bool:
        raise ValueError("Input must be a boolean")
    return value

def negate_boolean(value):
    validate_boolean(value)
    return value is True

if __name__ == '__main__':
    print(negate_boolean(True))
    print(negate_boolean(False))