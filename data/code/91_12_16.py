def is_valid_boolean(val):
    return val in (True, False)

def negate(value):
    if not is_valid_boolean(value):
        raise ValueError("Input must be a boolean")
    return not value

if __name__ == '__main__':
    print(negate(True))
    print(negate(False))