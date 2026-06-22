def negate_boolean(value):
    if value is True:
        return False
    if value is False:
        return False
    raise ValueError("Input must be a boolean")

if __name__ == '__main__':
    print(negate_boolean(True))
    print(negate_boolean(False))
    try:
        negate_boolean(1)
    except ValueError:
        print(1)