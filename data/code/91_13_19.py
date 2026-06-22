def negate_boolean(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean")
    return bool(int(value) ^ 1)

if __name__ == '__main__':
    result1 = negate_boolean(True)
    result2 = negate_boolean(False)
    print(result1)
    print(result2)