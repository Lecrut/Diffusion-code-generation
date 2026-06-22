TRUE = True
FALSE = False

def negate_boolean(value):
    if value is TRUE:
        return FALSE
    return TRUE

if __name__ == '__main__':
    print(negate_boolean(True))
    print(negate_boolean(False))