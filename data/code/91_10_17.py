def validate_boolean_input(value):
    if type(value) is not bool:
        raise ValueError("Input must be a boolean type")
    return value

def negate_boolean(value):
    validate_boolean_input(value)
    return value ^ True

if __name__ == '__main__':
    print(negate_boolean(True))
    print(negate_boolean(False))