TRUE_VAL = True
FALSE_VAL = False
INVERT_MAP = {True: False, False: True}

def invert_boolean(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean")
    return value ^ TRUE_VAL

if __name__ == '__main__':
    sample_values = [True, False, True, False]
    for val in sample_values:
        result = invert_boolean(val)
        print(result)