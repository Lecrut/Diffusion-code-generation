def _validate_boolean(value: object) -> bool:
    if not isinstance(value, bool):
        raise ValueError(f"Expected a boolean value, got {type(value).__name__}")
    return value

def negate_boolean(value: object) -> bool:
    validated = _validate_boolean(value)
    return not validated

if __name__ == '__main__':
    result_true = negate_boolean(True)
    result_false = negate_boolean(False)
    print(result_true)
    print(result_false)