def negate_boolean(value):
    if value is True:
        return False
    if value is False:
        return True
    raise ValueError("Input must be a boolean")

if __name__ == '__main__':
    print(negate_boolean(True))
    print(negate_boolean(False))