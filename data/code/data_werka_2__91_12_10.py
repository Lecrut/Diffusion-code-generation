NEGATE_MAP = {True: False, False: True}

def negate(value):
    return NEGATE_MAP[value]

if __name__ == '__main__':
    print(negate(True))
    print(negate(False))