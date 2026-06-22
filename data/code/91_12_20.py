def negate(value):
    if type(value) is not bool:
        raise ValueError("Input must be a boolean")
    return value ^ 1

if __name__ == '__main__':
    print(negate(True))
    print(negate(False))