def evaluate_expression(X, Y, Z, W):
    X = bool(X)
    Y = bool(Y)
    Z = bool(Z)
    W = bool(W)
    return (X and Y) or (Z and not W)

if __name__ == '__main__':
    result = evaluate_expression(True, False, True, True)
    print(result)