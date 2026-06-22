BOOLEAN_MAP = {True: False, False: True}

def negate_boolean(value):
    return BOOLEAN_MAP[value]

if __name__ == '__main__':
    print(negate_boolean(True))
    print(negate_boolean(False))