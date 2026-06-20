def validate_inputs(a: bool, b: bool, c: bool) -> None:
    if not isinstance(a, bool) or not isinstance(b, bool) or not isinstance(c, bool):
        raise ValueError('All inputs must be boolean')

def logical_and(A: bool, B: bool) -> bool:
    return A & B

def logical_or(A: bool, B: bool) -> bool:
    return A | B

def logical_not(C: bool) -> bool:
    return not C

if __name__ == '__main__':
    A_val = True
    B_val = False
    C_val = True
    validate_inputs(A_val, B_val, C_val)
    output_and = logical_and(A_val, B_val)
    output_or = logical_or(A_val, B_val)
    output_not = logical_not(C_val)
    print(output_and)
    print(output_or)
    print(output_not)