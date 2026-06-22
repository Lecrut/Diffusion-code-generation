def evaluate_logic(A, B, C, D):
    if not A and not C:
        return 0
    if not A:
        term1 = 0
    else:
        term1 = 1 if B else 0
    if not C:
        term2 = 0
    else:
        term2 = 1 if not D else 0
    return 1 if (term1 or term2) else 0

if __name__ == '__main__':
    A = 1
    B = 0
    C = 1
    D = 0
    result = evaluate_logic(A, B, C, D)
    print(result)