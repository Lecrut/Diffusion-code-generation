def invert_boolean(value: bool) -> bool:
    lookup: dict[bool, bool] = {True: False, False: True}
    return lookup[value]

if __name__ == '__main__':
    print(invert_boolean(True))
    print(invert_boolean(False))