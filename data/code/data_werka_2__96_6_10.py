def evaluate_logic(A, B, C, D):
    a = bool(A)
    b = bool(B)
    c = bool(C)
    d = bool(D)
    result = a and b or (c and (not d))
    return 1 if result else 0
if __name__ == '__main__':
    A = 1
    B = 0
    C = 1
    D = 0
    result = evaluate_logic(A, B, C, D)
    print(result)