TRUTH_TABLE = {True: False, False: True}

def negate_boolean(value):
    return TRUTH_TABLE[value]

if __name__ == '__main__':
    print(negate_boolean(True))
    print(negate_boolean(False))