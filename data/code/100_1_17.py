def check_logic(A, B, C):
    if not isinstance(A, bool) or not isinstance(B, bool) or not isinstance(C, bool):
        raise ValueError("All inputs must be boolean values.")
    
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