def evaluate_expression(A, B, C, D):
    return (A and B) or (C and not D)

if __name__ == '__main__':
    result = evaluate_expression(True, False, True, False)
    print(result)