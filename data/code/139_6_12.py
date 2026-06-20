def and_gate(a, b):
    if not isinstance(a, (int, str)) or not isinstance(b, (int, str)):
        raise TypeError('Inputs must be integers or binary strings.')
    if isinstance(a, str):
        a_val = int(a, 2)
    else:
        a_val = a
    if isinstance(b, str):
        b_val = int(b, 2)
    else:
        b_val = b
    return a_val & b_val

def or_gate(a, b):
    if not isinstance(a, (int, str)) or not isinstance(b, (int, str)):
        raise TypeError('Inputs must be integers or binary strings.')
    if isinstance(a, str):
        a_val = int(a, 2)
    else:
        a_val = a
    if isinstance(b, str):
        b_val = int(b, 2)
    else:
        b_val = b
    return a_val | b_val

def not_gate(a):
    if not isinstance(a, (int, str)):
        raise TypeError('Input must be an integer or binary string.')
    if isinstance(a, str):
        a_val = int(a, 2)
    else:
        a_val = a
    return ~a_val & 1

def xor_gate(a, b):
    if not isinstance(a, (int, str)) or not isinstance(b, (int, str)):
        raise TypeError('Inputs must be integers or binary strings.')
    if isinstance(a, str):
        a_val = int(a, 2)
    else:
        a_val = a
    if isinstance(b, str):
        b_val = int(b, 2)
    else:
        b_val = b
    return a_val ^ b_val
if __name__ == '__main__':
    print(and_gate('101', '110'))
    print(or_gate(1, 0))
    print(not_gate('0'))
    print(xor_gate('1', '0'))
    try:
        print(and_gate('101', 'invalid'))
    except TypeError as e:
        print(f'Error caught: {e}')
    try:
        print(OR(5, '2'))
    except TypeError as e:
        print(f'Error caught: {e}')