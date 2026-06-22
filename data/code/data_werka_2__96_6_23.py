def evaluate_logic(A, B, C, D):
    non_zero_A = 1 if A else 0
    non_zero_B = 1 if B else 0
    non_zero_C = 1 if C else 0
    non_zero_D = 1 if D else 0
    
    not_D = 1 - non_zero_D
    
    term1 = non_zero_A & non_zero_B
    term2 = non_zero_C & not_D
    
    result = term1 | term2
    
    return 1 if result else 0

if __name__ == '__main__':
    A = 1
    B = 0
    C = 1
    D = 0
    
    result = evaluate_logic(A, B, C, D)
    print(result)