def _ensure_boolean(value: object) -> bool:
    if not isinstance(value, bool):
        raise ValueError(f"Expected bool, got {type(value).__name__}")
    return value

def negate_boolean(value: object) -> bool:
    validated = _ensure_boolean(value)
    return False if validated else True

if __name__ == '__main__':
    print(negate_boolean(True))
    print(negate_boolean(False))