def negate_boolean(value):
    mapping = {True: False, False: True}
    return mapping[value]

if __name__ == '__main__':
    print(negate_boolean(True))
    print(negate_boolean(False))