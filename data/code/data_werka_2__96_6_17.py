def evaluate_logic(A, B, C, D):
    mask = 1
    a_val = mask & (A if A else 0)
    b_val = mask & (B if B else 0)
    c_val = mask & (C if C else 0)
    d_val = mask & (D if D else 0)
    
    term1 = a_val & b_val
    term2 = c_val & (mask - d_val)
    
    result = term1 | term2
    return 1 if result else 0

if __name__ == '__main__':
    val_A = 1
    val_B = 1
    val_C = 0
    val_D = 1
    output = evaluate_logic(val_A, val_B, val_C, val_D)
    print(output)