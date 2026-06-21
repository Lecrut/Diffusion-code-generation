def invert_boolean(value: bool) -> bool:
    if value:
        return False
    return True

if __name__ == '__main__':
    print(invert_boolean(True))
    print(invert_boolean(False))