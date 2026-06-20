def xor(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError('Inputs must be integers')
    return a ^ b

def and_gate(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError('Inputs must be integers')
    return a & b

def or_gate(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError('Inputs must be integers')
    return a | b

def not_gate(a):
    if not isinstance(a, int):
        raise ValueError('Input must be an integer')
    return ~a
if __name__ == '__main__':
    print(xor(1, 0))
    print(xor(10, 5))
    print(and_gate(1, 0))
    print(and_gate(10, 5))
    print(or_gate(1, 0))
    print(or_gate(10, 5))
    print(not_gate(1))
    print(not_gate(0))