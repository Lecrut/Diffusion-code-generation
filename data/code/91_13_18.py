NEGATE_MASK = 1

def negate_boolean(b):
    return bool(b ^ NEGATE_MASK)

if __name__ == '__main__':
    print(negate_boolean(True))
    print(negate_boolean(False))