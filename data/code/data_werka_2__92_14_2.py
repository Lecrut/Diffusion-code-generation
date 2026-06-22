def negate_boolean(value):
    lookup_table = {True: False, False: True}
    return lookup_table[value]

if __name__ == '__main__':
    print(negate_boolean(True))
    print(negate_boolean(False))