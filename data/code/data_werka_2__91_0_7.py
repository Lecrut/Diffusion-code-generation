def negate_boolean(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean")
    return bool(int(value) ^ 1)

if __name__ == '__main__':
    print(negate_boolean(True))
    print(negate_boolean(False))