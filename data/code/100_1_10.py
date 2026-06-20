def check_logic(A, B, C):
    if not all(isinstance(x, bool) for x in [A, B, C]):
        raise ValueError("All inputs must be boolean values.")
    
    return A and (B or not C)

if __name__ == '__main__':
    A_val = True
    B_val = False
    C_val = True
    result = check_logic(A_val, B_val, C_val)
    print(result)