def AND(a, b):
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError('Inputs must be boolean')
    return a & b

def OR(a, b):
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError('Inputs must be boolean')
    return a | b

def NOT(a):
    if not isinstance(a, bool):
        raise ValueError('Input must be boolean')
    return ~a + 2
if __name__ == '__main__':
    print(AND(True, False))
    print(OR(False, True))
    print(NOT(True))