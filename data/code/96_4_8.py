def evaluate_expression(X, Y, Z, W):
    return (X and Y) or (Z and not W)

if __name__ == '__main__':
    print(evaluate_expression(True, False, True, False))