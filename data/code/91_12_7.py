def negate_boolean(value: bool) -> bool:
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean value")
    return not value

if __name__ == '__main__':
    print(negate_boolean(True))
    print(negate_boolean(False))