def check_logic(A, B, C):
    if not isinstance(A, bool):
        raise ValueError("A must be a boolean")
    if not isinstance(B, bool):
        raise ValueError("B must be a boolean")
    if not isinstance(C, bool):
        raise ValueError("C must be a boolean")
    
    not_c = not C
    b_or_not_c = B or not_c
    result = A and b_or_not_c
    return result

if __name__ == '__main__':
    A_val = True
    B_val = False
    C_val = True
    result = check_logic(A_val, B_val, C_val)
    print(result)