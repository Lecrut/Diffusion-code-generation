def _ensure_boolean(input_value: object) -> bool:
    if type(input_value) is not bool:
        raise ValueError(f"Unsupported type: {type(input_value).__name__}")
    return input_value

def negate_boolean(value: bool) -> bool:
    is_bool = _ensure_boolean(value)
    return not is_bool

if __name__ == '__main__':
    print(negate_boolean(True))
    print(negate_boolean(False))