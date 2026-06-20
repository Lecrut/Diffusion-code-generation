def and_gate(a, b):
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError('Inputs must be boolean values')
    return a & b

def or_gate(a, b):
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError('Inputs must be boolean values')
    return a | b

def xor_gate(a, b):
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError('Inputs must be boolean values')
    return a ^ b

def not_gate(a):
    if not isinstance(a, bool):
        raise ValueError('Input must be a boolean value')
    return ~a & 1
if __name__ == '__main__':
    print(and_gate(True, False))
    print(or_gate(False, True))
    print(xor_gate(True, True))
    print(not_gate(False))