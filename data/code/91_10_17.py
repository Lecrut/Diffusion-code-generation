def negate_boolean(bool_val):
    if not isinstance(bool_val, bool):
        raise ValueError("Input must be a boolean")
    return not bool_val

if __name__ == '__main__':
    print(negate_boolean(True))
    print(negate_boolean(False))