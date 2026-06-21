def compute_logic(X, Y, Z, W):
    x = bool(X)
    if x:
        return bool(Y)
    z = bool(Z)
    if not z:
        return False
    w = bool(W)
    return not w

if __name__ == '__main__':
    X = False
    Y = False
    Z = True
    W = False
    result = compute_logic(X, Y, Z, W)
    print(result)