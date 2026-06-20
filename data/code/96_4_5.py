def evaluate_expression(X, Y, Z, W):
    try:
        return (X and Y) or (Z and not W)
    except TypeError as e:
        raise ValueError("All inputs must be boolean values") from e

if __name__ == '__main__':
    result = evaluate_expression(True, False, True, False)
    print(result)