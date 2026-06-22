INVERT_MAP = {True: False, False: True}

def invert_boolean(value: bool) -> bool:
    return INVERT_MAP[value]

if __name__ == '__main__':
    sample_true = True
    sample_false = False
    print(invert_boolean(sample_true))
    print(invert_boolean(sample_false))