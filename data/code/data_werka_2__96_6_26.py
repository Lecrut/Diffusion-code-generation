def evaluate_logic(A, B, C, D):
    A_bool = bool(A)
    B_bool = bool(B)
    C_bool = bool(C)
    D_bool = bool(D)
    
    term1 = A_bool and B_bool
    term2 = C_bool and (not D_bool)
    
    result = term1 or term2
    
    return 1 if result else 0

if __name__ == '__main__':
    A = 1
    B = 0
    C = 1
    D = 0
    
    result = evaluate_logic(A, B, C, D)
    print(result)