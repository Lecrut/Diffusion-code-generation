def validate_input(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean value")

def invert_boolean(value):
    validate_input(value)
    return value ^ True

if __name__ == '__main__':
    sample_values = [True, False]
    for val in sample_values:
        print(invert_boolean(val))