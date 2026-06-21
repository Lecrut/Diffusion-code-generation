def invert_boolean(value):
    lookup_table = {True: False, False: True}
    if value not in lookup_table:
        raise ValueError("Input must be a boolean")
    return lookup_table[value]

if __name__ == '__main__':
    print(invert_boolean(True))
    print(invert_boolean(False))