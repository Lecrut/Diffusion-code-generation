def invert_boolean(boolean_value: bool) -> bool:
    if not isinstance(boolean_value, bool):
        raise ValueError("Input must be a boolean value.")
    return not boolean_value

if __name__ == '__main__':
    sample_values = [True, False]
    for value in sample_values:
        print(invert_boolean(value))