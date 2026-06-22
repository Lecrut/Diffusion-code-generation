TRUE_VALUE = True
FALSE_VALUE = False

INVERSION_MAP = {
    True: False,
    False: True
}

def invert_boolean(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean")
    return value ^ TRUE_VALUE

if __name__ == '__main__':
    sample_values = [True, False]
    for val in sample_values:
        result = invert_boolean(val)
        print(result)