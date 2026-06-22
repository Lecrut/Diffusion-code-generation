def check_logic(A, B, C):
    if not isinstance(A, bool) or not isinstance(B, bool) or not isinstance(C, bool):
        raise ValueError("All inputs must be boolean values.")
    return A and (B or (not C))

def compute_expression(a, b, c):
    if not isinstance(a, bool) or not isinstance(b, bool) or not isinstance(c, bool):
        raise ValueError("Inputs must be boolean.")
    return a and (b or (not c))

if __name__ == '__main__':
    sample_A = True
    sample_B = False
    sample_C = True
    val_a = True
    val_b = True
    val_c = False
    result_primary = check_logic(sample_A, sample_B, sample_C)
    result_secondary = compute_expression(val_a, val_b, val_c)
    print(result_primary)
    print(result_secondary)