def _is_valid_boolean(input_value):
    return type(input_value) is bool

def negate_boolean(input_value):
    if not _is_valid_boolean(input_value):
        raise ValueError("Input must be a boolean")
    return not input_value

if __name__ == '__main__':
    print(negate_boolean(True))
    print(negate_boolean(False))