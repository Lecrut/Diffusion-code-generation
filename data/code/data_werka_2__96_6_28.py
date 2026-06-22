def evaluate_logic(A, B, C, D):
    mask = lambda x: -int(bool(x))
    term1 = mask(A) & mask(B)
    term2 = mask(C) & ~mask(D)
    result = term1 | term2
    return -((result >> 63) & 1) if result else 0

if __name__ == '__main__':
    A = 1
    B = 0
    C = 1
    D = 0
    print(evaluate_logic(A, B, C, D))