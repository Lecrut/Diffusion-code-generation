def negate_boolean(value: bool) -> bool:
    if not isinstance(value, bool):
        raise ValueError("Expected a boolean value")
    return bool(1 ^ value)

if __name__ == '__main__':
    print(negate_boolean(True))
    print(negate_boolean(False))