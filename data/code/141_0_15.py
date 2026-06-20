def validate_inputs(a, b, c):
    if not isinstance(a, bool) or not isinstance(b, bool) or not isinstance(c, bool):
        raise ValueError('All inputs must be boolean values')

def bitwise_and(a: bool, b: bool) -> bool:
    return a & b

def bitwise_or(a: bool, b: bool) -> bool:
    return a | b

def bitwise_not(a: bool) -> bool:
    return not a

def logic_gate(A, B, C):
    validate_inputs(A, B, C)
    result = (A and B) or (not C)
    return result

if __name__ == '__main__':
    A_val = True
    B_val = False
    C_val = True
    output = logic_gate(A_val, B_val, C_val)
    print(output)