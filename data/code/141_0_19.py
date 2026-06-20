def validate_inputs(A: bool, B: bool, C: bool) -> None:
    if not isinstance(A, bool) or not isinstance(B, bool) or (not isinstance(C, bool)):
        raise ValueError('All inputs must be boolean values.')

def bitwise_and(a: bool, b: bool) -> bool:
    return a & b

def bitwise_or(a: bool, b: bool) -> bool:
    return a | b

def bitwise_not(a: bool) -> bool:
    return not a

def evaluate_logic(A: bool, B: bool, C: bool, operation: str) -> bool:
    validate_inputs(A, B, C)
    if operation == 'AND':
        return bitwise_and(A, B)
    elif operation == 'OR':
        return bitwise_or(A, B)
    elif operation == 'NOT':
        return bitwise_not(C)
    else:
        raise ValueError('Invalid operation')
if __name__ == '__main__':
    A_val = True
    B_val = False
    C_val = True
    print(evaluate_logic(A_val, B_val, C_val, 'AND'))
    print(evaluate_logic(A_val, B_val, C_val, 'OR'))
    print(evaluate_logic(A_val, B_val, C_val, 'NOT'))