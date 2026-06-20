NEGATE_TRUE = False
NEGATE_FALSE = True

def negate_boolean(b):
    return b ^ NEGATE_TRUE

if __name__ == '__main__':
    print(negate_boolean(True))
    print(negate_boolean(False))