TRUTH_TABLE = {
    True: False,
    False: True
}

def invert_boolean(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean")
    return TRUTH_TABLE[value]

if __name__ == '__main__':
    sample_inputs = [True, False]
    for val in sample_inputs:
        result = invert_boolean(val)
        print(result)