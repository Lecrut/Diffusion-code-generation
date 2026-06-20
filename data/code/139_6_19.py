def AND(a, b):
    if isinstance(a, bool) and isinstance(b, bool):
        return a & b
    raise ValueError('Inputs must be boolean')

def OR(a, b):
    if isinstance(a, bool) and isinstance(b, bool):
        return a | b
    raise ValueError('Inputs must be boolean')

def NOT(a):
    if isinstance(a, bool):
        return not a
    raise ValueError('Input must be boolean')

def XOR(a, b):
    if isinstance(a, bool) and isinstance(b, bool):
        return a ^ b
    raise ValueError('Inputs must be boolean')
if __name__ == '__main__':
    print(AND(True, False))
    print(OR(False, True))
    print(NOT(True))
    print(XOR(True, True))