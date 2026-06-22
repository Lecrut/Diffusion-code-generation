NEGATE_TRUE = True
NEGATE_FALSE = False

def negate(value):
    if value is True:
        return NEGATE_FALSE
    return NEGATE_TRUE

if __name__ == '__main__':
    print(negate(True))
    print(negate(False))