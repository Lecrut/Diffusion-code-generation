def evaluate_expression(X, Y, Z, W):
    if not all(isinstance(i, bool) for i in [X, Y, Z, W]):
        raise ValueError("All inputs must be boolean values")
    return (X and Y) or (Z and not W)

if __name__ == '__main__':
    result = evaluate_expression(True, False, True, False)
    print(result)