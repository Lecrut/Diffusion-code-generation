BOOL_INVERT = {True: False, False: True}

def invert_boolean(value: bool) -> bool:
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean")
    return BOOL_INVERT[value]

if __name__ == '__main__':
    print(invert_boolean(True))
    print(invert_boolean(False))