def check_logic(A, B, C):
    if not isinstance(A, bool) or not isinstance(B, bool) or not isinstance(C, bool):
        raise ValueError("Inputs must be boolean")
    return A and (B or (not C))

if __name__ == '__main__':
    A_val = True
    B_val = False
    C_val = True
    result = check_logic(A_val, B_val, C_val)
    print(result)