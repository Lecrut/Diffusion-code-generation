def evaluate_nested_logic(a, b, c, d):
    ab = a and b
    cd_not_d = c and not d
    result = ab or cd_not_d
    return result

if __name__ == '__main__':
    X = True
    Y = False
    Z = False
    W = True
    outcome = evaluate_nested_logic(X, Y, Z, W)
    print(outcome)