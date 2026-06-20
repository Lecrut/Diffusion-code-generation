def validate_boolean(value):
    if not isinstance(value, bool):
        raise ValueError("All inputs must be boolean values")

def evaluate_expression(X, Y, Z, W):
    validate_boolean(X)
    validate_boolean(Y)
    validate_boolean(Z)
    validate_boolean(W)
    return (X and Y) or (Z and not W)

if __name__ == '__main__':
    result = evaluate_expression(True, False, True, False)
    print(result)