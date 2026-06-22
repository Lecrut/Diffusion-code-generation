def evaluate_logic(X, Y, Z, W):
    a = bool(X)
    b = bool(Y)
    c = bool(Z)
    d = not bool(W)
    term1 = a and b
    term2 = c and d
    return term1 or term2

if __name__ == '__main__':
    val_X = 1
    val_Y = 0
    val_Z = 0
    val_W = 1
    computed_result = evaluate_logic(val_X, val_Y, val_Z, val_W)
    print(computed_result)