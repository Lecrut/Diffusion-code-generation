def negate(value):
    if value is True:
        return False
    if value is False:
        return True
    raise ValueError("Input must be a boolean")

if __name__ == '__main__':
    print(negate(True))
    print(negate(False))