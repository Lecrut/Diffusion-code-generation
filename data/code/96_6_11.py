def evaluate_logic(A, B, C, D):
    non_zero = lambda x: bool(x)
    a = non_zero(A)
    b = non_zero(B)
    c = non_zero(C)
    d = non_zero(D)
    
    term1 = a and b
    term2 = c and (not d)
    
    result = term1 or term2
    
    return 1 if result else 0

if __name__ == '__main__':
    A = 1
    B = 0
    C = 1
    D = 0
    
    result = evaluate_logic(A, B, C, D)
    print(result)