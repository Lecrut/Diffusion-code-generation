def evaluate_expression(X, Y, Z, W):
    bool_X = bool(X)
    bool_Y = bool(Y)
    bool_Z = bool(Z)
    bool_W = bool(W)
    result = (bool_X and bool_Y) or (bool_Z and (not bool_W))
    return result

if __name__ == '__main__':
    X = True
    Y = False
    Z = False
    W = True
    result = evaluate_expression(X, Y, Z, W)
    print(result)