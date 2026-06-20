def evaluate_expression(X: bool, Y: bool, Z: bool, W: bool) -> bool:
    return (X and Y) or (Z and not W)

if __name__ == '__main__':
    result = evaluate_expression(True, False, True, False)
    print(result)