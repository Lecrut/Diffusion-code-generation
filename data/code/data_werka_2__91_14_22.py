def _validate_boolean_input(value: object) -> bool:
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean type")
    return value

def flip_bool_value(value: bool) -> bool:
    _validate_boolean_input(value)
    return not value

if __name__ == '__main__':
    print(flip_bool_value(True))
    print(flip_bool_value(False))