def evaluate_logic(A, B, C, D):
    A_bool = A != 0
    B_bool = B != 0
    C_bool = C != 0
    D_bool = D != 0
    not_D = not D_bool
    term1 = A_bool and B_bool
    term2 = C_bool and not_D
    result = term1 or term2
    return 1 if result else 0

if __name__ == '__main__':
    A = 1
    B = 0
    C = 1
    D = 0
    result = evaluate_logic(A, B, C, D)
    print(result)