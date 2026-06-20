def invert_boolean(boolean_input):
    if not isinstance(boolean_input, bool):
        raise ValueError("Input must be a boolean value")
    return not boolean_input

if __name__ == '__main__':
    sample_value = True
    print(invert_boolean(sample_value))