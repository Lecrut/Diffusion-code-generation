def evaluate_expression(A, B, C, D):
    return (A and B) or (C and not D)
if __name__ == '__main__':
    A_val = True
    B_val = False
    C_val = True
    D_val = False
    result = evaluate_expression(A_val, B_val, C_val, D_val)
    print(result)