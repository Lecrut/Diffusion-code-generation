def validate_boolean(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean value")

def print_logical_opposite(boolean_value):
    validate_boolean(boolean_value)
    inverted_value = ~int(boolean_value)
    print(inverted_value)

if __name__ == '__main__':
    print_logical_opposite(True)
    print_logical_opposite(False)