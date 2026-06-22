def evaluate_logic(A, B, C, D):
    bool_A = A != 0
    bool_B = B != 0
    bool_C = C != 0
    bool_D = D != 0
    
    term1 = bool_A and bool_B
    term2 = bool_C and (not bool_D)
    
    result = term1 or term2
    return 1 if result else 0

if __name__ == '__main__':
    A = 1
    B = 0
    C = 1
    D = 0
    
    result = evaluate_logic(A, B, C, D)
    print(result)