def _validate_bool_input(value: object) -> None:
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean type")

def flip_bool_value(value: bool) -> bool:
    _validate_bool_input(value)
    return not value

if __name__ == '__main__':
    print(flip_bool_value(True))
    print(flip_bool_value(False))