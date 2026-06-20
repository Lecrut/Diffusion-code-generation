def validate_input(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean")

def print_logical_opposite(boolean_value):
    validate_input(boolean_value)
    print(not boolean_value)

if __name__ == '__main__':
    print_logical_opposite(True)
    print_logical_opposite(False)