def invert_boolean(value):
    inversion_map = {True: False, False: True}
    return inversion_map[value]

if __name__ == '__main__':
    print(invert_boolean(True))
    print(invert_boolean(False))