TRUE_MAP = {True: False, False: True}

def negate_boolean(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean")
    return TRUE_MAP[value]

if __name__ == '__main__':
    sample_values = [True, False]
    for val in sample_values:
        result = negate_boolean(val)
        print(result)