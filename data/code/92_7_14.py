BOOL_INVERSION_MAP = {True: False, False: True}

def invert_boolean(value: bool) -> bool:
    if value in BOOL_INVERSION_MAP:
        return BOOL_INVERSION_MAP[value]
    raise ValueError("Input must be a boolean")

if __name__ == '__main__':
    sample_value = True
    print(invert_boolean(sample_value))
    sample_value = False
    print(invert_boolean(sample_value))