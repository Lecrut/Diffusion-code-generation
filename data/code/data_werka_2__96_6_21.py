def evaluate_logic(A, B, C, D):
    non_zero_A = bool(A)
    non_zero_B = bool(B)
    non_zero_C = bool(C)
    non_zero_D = bool(D)
    
    term1 = non_zero_A and non_zero_B
    term2 = non_zero_C and (not non_zero_D)
    
    result = term1 or term2
    
    return 1 if result else 0

if __name__ == '__main__':
    A = 1
    B = 0
    C = 1
    D = 0
    
    result = evaluate_logic(A, B, C, D)
    print(result)