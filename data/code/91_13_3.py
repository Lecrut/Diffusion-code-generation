def negate_boolean(b):
    if not isinstance(b, bool):
        raise ValueError("Input must be a boolean.")
    return b ^ True

if __name__ == '__main__':
    print(negate_boolean(True))
    print(negate_boolean(False))