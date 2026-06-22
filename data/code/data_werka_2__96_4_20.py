def evaluate_logic(X, Y, Z, W):
    bool_X = bool(X)
    bool_Y = bool(Y)
    bool_Z = bool(Z)
    bool_W = bool(W)
    
    term1 = bool_X and bool_Y
    if term1:
        return True
    
    term2 = bool_Z and (not bool_W)
    return term2

if __name__ == '__main__':
    X = False
    Y = True
    Z = True
    W = False
    result = evaluate_logic(X, Y, Z, W)
    print(result)