NOT_BOOL = TypeError("Input must be a boolean value")

def negate_boolean(value):
    if not isinstance(value, bool):
        raise NOT_BOOL
    return not value

if __name__ == '__main__':
    print(negate_boolean(True))
    print(negate_boolean(False))