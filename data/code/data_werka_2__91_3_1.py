def invert_boolean(value: bool) -> bool:
    return bool(value ^ 1)

if __name__ == '__main__':
    print(invert_boolean(True))
    print(invert_boolean(False))