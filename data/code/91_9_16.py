def negate_boolean(value):
    if not isinstance(value, bool):
        raise ValueError('Input must be a boolean value')
    return not value
if __name__ == '__main__':
    try:
        print(negate_boolean(True))
        print(negate_boolean(False))
        print(negate_boolean(123))
    except ValueError as e:
        print(e)