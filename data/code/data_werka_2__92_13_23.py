def invert_boolean(value: bool) -> bool:
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean")
    return value ^ True

if __name__ == '__main__':
    print(invert_boolean(True))
    print(invert_boolean(False))
    print(invert_boolean(True) == False)
    print(invert_boolean(False) == True)
    print(invert_boolean(True) is not False)
    print(invert_boolean(False) is not True)