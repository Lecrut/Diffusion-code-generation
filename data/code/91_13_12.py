NEGATE_CONST = True

def negate_boolean(b):
    return b ^ NEGATE_CONST

if __name__ == '__main__':
    print(negate_boolean(True))
    print(negate_boolean(False))