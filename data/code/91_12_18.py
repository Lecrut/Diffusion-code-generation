def negate(value: bool) -> bool:
    if type(value) is not bool:
        raise ValueError("Input must be a boolean")
    if value:
        return False
    return True

if __name__ == '__main__':
    print(negate(True))
    print(negate(False))