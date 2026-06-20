def is_valid_boolean(value):
    return isinstance(value, bool)

def invert_boolean(value):
    if not is_valid_boolean(value):
        raise ValueError("Input must be a boolean value.")
    return value ^ True

if __name__ == '__main__':
    sample_values = [True, False]
    for val in sample_values:
        print(invert_boolean(val))