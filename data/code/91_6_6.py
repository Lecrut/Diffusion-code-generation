def _ensure_boolean(value: object) -> bool:
    if type(value) is not bool:
        raise ValueError(f"Expected bool, got {type(value).__name__}")
    return value

def negate_boolean(value: object) -> bool:
    validated = _ensure_boolean(value)
    return validated ^ True

if __name__ == '__main__':
    true_result = negate_boolean(True)
    false_result = negate_boolean(False)
    print(true_result)
    print(false_result)