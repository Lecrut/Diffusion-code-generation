def invert_boolean(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean")
    result = value ^ True
    return result

if __name__ == '__main__':
    sample_value = True
    inverted = invert_boolean(sample_value)
    print(inverted)
    sample_value = False
    inverted = invert_boolean(sample_value)
    print(inverted)