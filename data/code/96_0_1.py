def evaluate_expression(A, B, C, D):
    result = (A and B) or (C and not D)
    return result
if __name__ == '__main__':
    A = True
    B = False
    C = True
    D = False
    result = evaluate_expression(A, B, C, D)
    print(result)