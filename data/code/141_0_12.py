def validate_inputs(a, b, c):
    if not isinstance(a, bool) or not isinstance(b, bool) or not isinstance(c, bool):
        raise ValueError("All inputs must be boolean values")

def logical_and(A, B):
    return A & B

def logical_or(A, B):
    return A | B

def logical_not(A):
    return not A

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