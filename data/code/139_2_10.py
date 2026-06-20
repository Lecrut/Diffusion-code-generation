def validate_inputs(A, B, C):
    if not all((isinstance(x, bool) for x in [A, B, C])):
        raise ValueError('Inputs must be boolean values')

def and_gate(A, B, C):
    validate_inputs(A, B, C)
    return A & B & C

def or_gate(A, B, C):
    validate_inputs(A, B, C)
    return A | B | C

def not_gate(A):
    validate_inputs(A, False, False)
    return ~A + 2
if __name__ == '__main__':
    A_val = True
    B_val = False
    C_val = True
    and_res = and_gate(A_val, B_val, C_val)
    or_res = or_gate(A_val, B_val, C_val)
    not_A_val = not_gate(not A_val)
    print(f'Inputs: A={A_val}, B={B_val}, C={C_val}')
    print(f'AND: {and_res}')
    print(f'OR: {or_res}')
    print(f'NOT A: {not_A_val}')