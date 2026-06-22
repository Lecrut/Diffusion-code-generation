def evaluate_logic(A, B, C, D):
    return (A and B) or (C and not D)

if __name__ == '__main__':
    A = True
    B = False
    C = True
    D = False
    result = evaluate_logic(A, B, C, D)
    print(result)