def evaluate_logic(X, Y, Z, W):
    bool_map = {
        'X': bool(X),
        'Y': bool(Y),
        'Z': bool(Z),
        'W': bool(W)
    }
    
    term1 = bool_map['X'] and bool_map['Y']
    term2 = bool_map['Z'] and (not bool_map['W'])
    
    return term1 or term2

if __name__ == '__main__':
    X = 1
    Y = 0
    Z = 1
    W = 0
    result = evaluate_logic(X, Y, Z, W)
    print(result)