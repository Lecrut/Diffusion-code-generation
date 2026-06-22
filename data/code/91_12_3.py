def negate(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean")
    return value ^ True

if __name__ == '__main__':
    print(negate(True))
    print(negate(False))