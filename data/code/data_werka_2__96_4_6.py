def evaluate_expression(X, Y, Z, W):
    X_bool = bool(X)
    Y_bool = bool(Y)
    Z_bool = bool(Z)
    W_bool = bool(W)
    
    if not all(isinstance(v, bool) for v in [X_bool, Y_bool, Z_bool, W_bool]):
        raise ValueError("Inputs must be convertible to boolean")
        
    result = (X_bool and Y_bool) or (Z_bool and (not W_bool))
    return result

if __name__ == '__main__':
    X = True
    Y = False
    Z = False
    W = True
    result = evaluate_expression(X, Y, Z, W)
    print(result)