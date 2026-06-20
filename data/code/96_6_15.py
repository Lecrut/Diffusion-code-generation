def evaluate_logic(A, B, C, D):
    return (A & B) | (C & ~D)

if __name__ == '__main__':
    A = 1
    B = 0
    C = 1
    D = 0
    print(evaluate_logic(A, B, C, D))