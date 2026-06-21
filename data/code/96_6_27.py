def evaluate_logic(A, B, C, D):
    mask = 1
    a_val = 1 if A else 0
    b_val = 1 if B else 0
    c_val = 1 if C else 0
    d_val = 1 if D else 0
    not_d = mask & ~d_val
    term1 = a_val & b_val
    term2 = c_val & not_d
    result = term1 | term2
    return result

if __name__ == '__main__':
    val_A = 0
    val_B = 5
    val_C = 3
    val_D = 2
    output = evaluate_logic(val_A, val_B, val_C, val_D)
    print(output)